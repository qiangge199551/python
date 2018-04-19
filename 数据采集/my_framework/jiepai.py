import requests
from requests import exceptions
# from urllib.parse import urlencode
import os
import re
import json

# from time import sleep
# from tqdm import tqdm
# def progressbar():
# 	for i in tqdm(range(1000)):
# 		sleep(0.01)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
def get_url(url, offset):
	query = {
		'offset': offset,
		'format': 'json',
		'keyword': '街拍',
		'autoload': 'true',
		'count': '20',
		'cur_tab': '1',
		'from': 'search_tab',
	}
	try:
		session = requests.Session()
		response = session.get(url, params=query, timeout=30)
		response.raise_for_status()
		# print(response.status_code, response.url, response.request.headers, response.encoding, response.apparent_encoding)
		print(response.text)
		return response
	except exceptions.ConnectionError as e:
		print(e)


def get_object(response):
	response_json = json.loads(response.text)
	img_url = []
	# if response_json['data']:
	for item in response_json['data']:
		try:
			yield {
				'img_list': img_url.append(item_['img_url'] for item_ in item['results']),
				'title': item['title'],
			}
		except:
			continue


def output_object(image_detail):
# try:
	for img_url in image_detail['img_list']:
		response = requests.get(img_url, headers=headers, timeout=10)
		response.raise_for_status()
		fpath = 'image/' + image_detail['title'] +'/' + '{0}.jpg'.format(img_url.split('/')[-1])
		if not os.path.exists('image/' + image['title']):
			os.mkdir('image/' + image_detail['title'])
		if not os.path.exists(fpath):
			with open(fpath, 'wb') as f:
				f.write(response.content)
# except:
#     print('output_object ERROR')


def main():
	# progressbar()
	root_url = 'https://www.toutiao.com/search_content/'
	for offset in range(0, 30, 10)
		response = get_url(root_url, offset=offset)
		for image_detail in get_object(response):
			output_object(image_detail)
		# print(html)


if __name__ == '__main__':
	main()