import requests
from requests import exceptions
from urllib.parse import urlencode
import urllib
import re

import time
import random
import linecache
from fake_useragent import UserAgent

ip_path = '../ip'

class get_html(object):
	"""docstring for get_html"""
	def __init__(self, url, headers=None, params=None, data=None, cookies=None):
		self.url = url
		self.headers = {}
		self.headers['User-Agent'] = UserAgent().random
		self.headers["Host"]="www.zhihu.com"
		self.headers["Referer"]="www.zhihu.com"
		# with open(ip_path, 'r') as f:
		# 	line = random.randrange(0, len(f.readlines()))
		# 	self.proxies = {'http': linecache.getline(ip_path, line)}
		# 	linecache.checkcache(filename=None)
		self.params = params
		self.data = data
		self.cookies = {}
		cookies = '_xsrf=cbdc66cc-c2f9-4e8c-a01d-6e74b65dc339; q_c1=ab0fdf4bdb484362abb3c97910cf6ee9|1518165718000|1518165718000; _zap=044948c8-6f86-4995-83f1-c2ade7dd1c25; d_c0="ANDsEhV5Hw2PTugAwF5adWJhwk4quIE5hqw=|1518230415"; l_cap_id="NzFkNDg3YTU2NTQ4NGIyYmFlNDhmMTNmZjZjYzgwYTE=|1519521968|806966ed06c5987fc4abd890797a92b69528a13a"; r_cap_id="ODhlYjVhMWM4N2M4NDM1ZWFmYWM4YWZkYmVhZDEwYjM=|1519521968|5f8308672fc998abe9f19eb78e78beaa14b3f468"; cap_id="ZjAyMjg1MjFlNjEwNDQ3NDg0OTIxNjVlM2VlNGRiZDc=|1519521968|83a709bbaf74fcd9ba906f61287b2cf0ca6c22d3"; __utma=51854390.412444244.1520238725.1520238725.1520238725.1; __utmc=51854390; __utmz=51854390.1520238725.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; __utmv=51854390.100--|2=registration_date=20160811=1^3=entry_date=20160811=1; capsion_ticket="2|1:0|10:1520431689|14:capsion_ticket|44:YzBlZjE3M2Y0ZjYwNDJkY2E5ZTA2NzY4MWUyMDIwZWU=|77255999553b068cd98b88298b8a874714f07e83b84432bce5cddbdf15779e19"; z_c0="2|1:0|10:1520431700|4:z_c0|92:Mi4xWmJWWUF3QUFBQUFBME93U0ZYa2ZEU1lBQUFCZ0FsVk5WRUNOV3dCWW9reHpNckI3eml2bzRnalVfeUtTa3l4bHNn|cc019d00c78e6f57a634bbaf74fd147678c2888a9d05879ed334a991e2a4c3a1"'
		for line in cookies.split(';'):
			key, vaule = line.split('=', 1)
			self.cookies[key] = vaule

	def response_html(self, encoding='utf-8'):
		# url = url + urlencode(self.params)
		try:
			# time.sleep(random.randrange(0,15))
			# ses = requests.Session()
			response = requests.get(url=self.url, headers=self.headers, proxies=None, cookies=self.cookies, params=self.params, data=self.data, verify=True, allow_redirects=True)
			response.raise_for_status()
			# print(response.request.headers, response.encoding)
			response.encoding = encoding
			with open('zhihu.txt', 'w') as f:
				f.write(str(response.text))
			return response.text
		except exceptions.Timeout as e:
			print(e)
		except exceptions.HTTPError as e:
			print(e)
		except exceptions.ConnectionError as e:
			print(e)

class get_object(object):
	"""docstring for get_object"""
	def __init__(self, response):
		self.profile = {}
		self.profile['user_name'] = ''
		self.profile['fuser_gender'] = ''
		self.profile['user_location'] =''
		self.profile['user_followees'] = ''
		self.profile['user_followers'] = ''
		self.profile['user_be_agreed'] = ''
		self.profile['user_be_thanked'] = ''
		self.profile['user_education_school'] = ''
		self.profile['user_education_subject'] = ''
		self.profile['user_employment'] = ''
		self.profile['user_employment_extra'] = ''
		self.profile['user_info'] = ''
		self.profile['user_intro'] = ''

		self.response = response

	def parse_html(self):
		# <span class="ProfileHeader-name" data-reactid="72">维斯特帕列</span>
		name_re = re.compile(r'class="ProfileHeader-name".*?">(.+?)</span>', re.S)
		self.profile['user_name'] = re.findall(name_re, str(self.response))
	def output_object(self):
		print(str(self.profile['user_name']))
		

def main():
	url = 'https://www.zhihu.com/people/aaronli-yu-er/activities'
	response = get_html(url).response_html()
	get_object(response).parse_html()

if __name__ == '__main__':
	main()
		


		