import requests
from requests import exceptions
from urllib.parse import urlencode
from fake_useragent import UserAgent
import time
import random
from tqdm import tqdm
import pymongo

def progressbar():
	for i in tqdm(range(1000)):
		time.sleep(0.01)

def get_response(url, page, encoding='utf-8'):
	for num in range(0, 15):
		ran = random.randint(1, 3)
		time.sleep(ran)
	headers = {
		'Host': 'www.lagou.com',
		'Origin': 'https://www.lagou.com',
		'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
		'User-Agent': UserAgent().random,
	}
	query = {'city': '杭州', 'needAddtionalResult': 'false', 'isSchoolJob': '0'}
	url = url + urlencode(query)
	# print(url)
	data = {'first': 'true', 'pn': page, 'kd': 'python'}
	try:
		session = requests.Session()
		response = session.post(url, headers=headers, data=data)
		# response.raise_for_status()
		# print(response.status_code, response.request.headers, response.apparent_encoding, response.text)
		headers.update(response.cookies)
		response.encoding = encoding
		return response
	except exceptions.Timeout as e:
		print('get_url ERROR', e)
	except exceptions.HTTPError as e:
		print('get_url ERROR', e)
	except exceptions.ConnectionError as e:
		print('get_url ERROR', e)

def get_object(response):
	response_json = response.json()
	for results in response_json['content']['positionResult']['result']:
		# print(results['city'], results['district'], results['companyFullName'], results['firstType'], results['education'], results['createTime'],)
		try:
			result = {
				'Workplace': results['city'] + str(results['district']),
				'Company Full Name': results['companyFullName'],
				'createtime': results['createTime'],
				'education': results['education'],
				'firstType': results['firstType'],
			}
			print('-------------------------------------------')
			print(result)
			save_to_mongo(result)
		except:
			continue

def save_to_mongo(result):
	client = pymongo.MongoClient('localhost')
	db = client['lagou']
	try:
		if db['Python_job'].insert(result):
			print('SAVE TO MONGODB SUCCESSFULLY')
	except Exception:
		print('FAIL TO SAVE TO MONGODB')

def main():
	# progressbar()
	root_url = 'https://www.lagou.com/jobs/positionAjax.json?'
	for page in range(1, 6):
		response = get_response(root_url, page)
		get_object(response)

if __name__ == '__main__':
	main()
