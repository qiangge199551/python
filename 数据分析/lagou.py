'''
title：lagou可视化
time:2018-4-8
'''
import requests
from requests import exceptions
from urllib.parse import urlencode
import re
import pymongo
from config import *
import time,random

import pandas as pd


class CRAWLER(object):
	"""docstring for CRAWLER"""
	def __init__(self):
		self.headers = {
			'Host': 'www.lagou.com',
			'Origin': 'https://www.lagou.com',
			'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
		}
		self.query = {'city': CITY, 'needAddtionalResult': 'false', 'isSchoolJob': '0'}

	def get_response(self, page, encoding='utf-8'):
		url = root_url + urlencode(self.query)
		# print(url)
		data = {'first': 'true', 'pn': page, 'kd': JOB}
		try:
			time.sleep(random.randint(2, 5))
			session = requests.Session()
			response = session.post(url, headers=self.headers, data=data)
			# response.raise_for_status()
			# print(response.status_code, response.request.headers, response.apparent_encoding, response.text)
			self.headers.update(response.cookies)
			response.encoding = encoding
			return response
		except exceptions.ConnectionError as e:
			print(e)

	def get_object(self, response):
		# json转dict获取内容
		# client = pymongo.MongoClient(MONGO_URL)
		# db = client[MONGO_DB]
		# response_json = response.json()
		# print('??????????????????????????????????????\n\n', response_json)
		# count = 0
		# for results in response_json['content']['positionResult']['result']:
		# 	# print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n', results)
		# 	count += 1
		# 	try:
		# 		result = {
		# 			# 'Workplace': results['city'] + str(results['district']),
		# 			'Company Full Name': results['companyFullName'],
		# 			'createtime': results['createTime'],
		# 			'education': results['education'],
		# 			'firstType': results['firstType'],
		# 		}
		# 		print('---------------------------------------------------------')			
		# 		print(result)
		# 		db[MONGO_TABLE].insert(result)
		# 		print('PAGE: {0} | NUMBER: {1} | SAVE TO MONGODB SUCCESSFULLY'.format(page, count))
		# 	except:
		# 		print('PAGE: {0} | NUMBER: {1} |  FAIL TO SAVE TO MONGODB'.format(page, count))
		# 		continue
		
		# 正则表达式提取内容
		datas = re.findall('"positionName":"(.*?)","workYear":"(.*?)","education":"(.*?)","jobNature".*?"createTime":"(.*?)","score":.*?"city":"(.*?)","salary":"(.*?)","approve":.*?"district":"(.*?)","companyLogo":.*?"companyFullName":"(.*?)","imState".*?"firstType":"(.*?)","secondType":"(.*?)","isSchoolJob":.*?}', response.text)
		data = pd.DataFrame(datas)
		data.to_csv('./lagoudata.csv', header=False, index=False, mode='a+')


def main():
	response = CRAWLER().get_response(1)
	CRAWLER().get_object(response)
	

if __name__ == '__main__':
	main()