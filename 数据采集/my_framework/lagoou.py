import requests
import time,random
import pymongo


def get_response(job, pn, session):
	url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
	time.sleep(random.randint(1, 5))
	headers = {
		'Host': 'www.lagou.com',
		'Origin': 'https://www.lagou.com',
		'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
	}
	query = {'px': 'default', 'needAddtionalResult': 'false'}
	data = {'first': 'true', 'pn': pn, 'kd': job}
	try:
		response = session.post(url, headers=headers, data=data)
		response.raise_for_status()
		# print(response.status_code, response.request.headers, response.apparent_encoding, response.text)
		# headers.update(response.cookies)
		return response
	except requests.exceptions.ConnectionError as e:
		print('get_url ERROR', e)

def get_object(response):
	response_json = response.json()
	for results in response_json['content']['positionResult']['result']:
		# print(results['city'], results['district'], results['companyFullName'], results['firstType'], results['education'], results['createTime'],)
		try:
			result = {
				'Workplace': results['city'],
				'Company Full Name': results['companyFullName'],
				'positionName': results['positionName'],
				'salary': results['salary'],
				'workYear': results['workYear'],
				# 'createtime': results['createTime'],
				'education': results['education'],
				'firstType': results['firstType'],
				'secondType': results['secondType'],
				'positionLables': results['positionLables'],
			}
			save_to_mongo(result)
		except:
			continue

def save_to_mongo(result):
	client = pymongo.MongoClient('localhost')
	db = client['JOB']
	try:
		if db['lagou_python'].insert(result):
			print(result, '\nSAVE TO MONGODB SUCCESSFULLY', '\n-----------------------------------------------\n\n')
	except Exception:
		print(result, '\nFAIL TO SAVE TO MONGODB', '\n-----------------------------------------------\n\n')

def main():
	session = requests.Session()
	for pn in range(1, 30):
		response = get_response(job='python', pn=pn, session=session)
		get_object(response)

if __name__ == '__main__':
	main()
