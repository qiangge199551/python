import requests
import re
import json


def get_url_text(url, encoding='utf-8'):
	try:
		headers = {
			'Cookie': 'uuid=1A6E888B4A4B29B16FBA1299108DBE9C8FE00275969081614A6803F493C0A9B5; _csrf=a4c034dc6b6d0d5377fe7e5c6b5cbe7dbbbceef33cf406b8253cb9cd17d67d47; __mta=208428973.1520240032694.1520240032694.1520240032694.1; _lxsdk_s=38dbe2aa74162e7dea207c8361bf%7C%7C3',
			'Host': 'maoyan.com',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
		}
		session = requests.Session()
		response = session.get(url, headers=headers, timeout=30)
		response.raise_for_status()
		# print(response.status_code, response.request.headers, response.encoding, response.apparent_encoding)
		response.encoding = encoding
		return response.text
	except:
		print('get_url_text ERROR')

def get_url_info(html):
	pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
						 + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
						 + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
	items = re.findall(pattern, html)
	for item in items:
		yield {
			'index': item[0],
			'image': item[1],
			'title': item[2].strip(),
			'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
			'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
			'score': item[5].strip() + item[6].strip()
		}

def main():
	url = r'http://maoyan.com/board/4?offset=20'
	html = {}
	fpath = 'E:\python\scrapy\maoyan_Top100\Top100.txt'
	html = get_url_text(url)
	for item in get_url_info(html):
		with open(fpath, 'a', encoding='utf-8') as f:
			f.write(json.dumps(item, ensure_ascii=False) + '\n')


if __name__ == '__main__':
	main()
