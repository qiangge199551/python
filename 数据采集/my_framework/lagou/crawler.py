import requests
from requests import exceptions
from urllib.parse import urlencode
from fake_useragent import UserAgent
import time
import random
from config import *
import pymongo


class CRAWLER(object):
	"""docstring for CRAWLER"""
	def __init__(self):
		self.headers = {
			'Host': 'www.lagou.com',
			'Origin': 'https://www.lagou.com',
			'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
			'User-Agent': UserAgent().random,
		}
		self.query = {'city': CITY, 'needAddtionalResult': 'false', 'isSchoolJob': '0'}
		self.proxies = {
			# 'https': r'https://115.211.69.219',
			'jttp': r'http://219.219.254.163',	
		}

	def get_response(self, page, encoding='utf-8'):
		url = root_url + urlencode(self.query)
		# print(url)
		data = {'first': 'true', 'pn': page, 'kd': JOB}
		try:
			session = requests.Session()
			response = session.post(url, headers=self.headers, proxies=self.proxies, data=data)
			# response.raise_for_status()
			# print(response.status_code, response.request.headers, response.apparent_encoding, response.text)
			self.headers.update(response.cookies)
			response.encoding = encoding
			return response
		except exceptions.ConnectionError as e:
			print(e)

	def get_object(self, response, page):
		client = pymongo.MongoClient(MONGO_URL)
		db = client[MONGO_DB]
		response_json = response.json()
		# print('??????????????????????????????????????\n\n', response_json)
		count = 0
		for results in response_json['content']['positionResult']['result']:
			# print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n', results)
			count += 1
			try:
				result = {
					# 'Workplace': results['city'] + str(results['district']),
					'Company Full Name': results['companyFullName'],
					'createtime': results['createTime'],
					'education': results['education'],
					'firstType': results['firstType'],
				}
				print('---------------------------------------------------------')			
				print(result)
				db[MONGO_TABLE].insert(result)
				print('PAGE: {0} | NUMBER: {1} | SAVE TO MONGODB SUCCESSFULLY'.format(page, count))
			except:
				print('PAGE: {0} | NUMBER: {1} |  FAIL TO SAVE TO MONGODB'.format(page, count))
				continue
def start(page):
	# progressbar()
	response = CRAWLER().get_response(page)
	CRAWLER().get_object(response, page)

