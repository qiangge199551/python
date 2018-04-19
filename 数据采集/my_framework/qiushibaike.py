import requests
from bs4 import BeautifulSoup
import re

def get_html_text(url, encoding='utf-8'):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
	try:
		response = requests.get(url, headers=headers, timeout=10)
		response.raise_for_status()
		response.encoding = encoding
		# print(response.status_code, response.request.headers, response.encoding, response.apparent_encoding)
	except:
		print('get_html_text ERROR')
	return response

def html_parser(url):
	slist = []
	response = get_html_text(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	print(soup)
	print(soup.find_all('div', attrs={'class': 'content'}))
	for tag in soup.find_all('div', attrs={'class': 'content'}):
		try:
			slist.append(tag.string)
			print(tag.string)
		except:
			continue
	return slist

def html_outputer(slist, fpath):
	with open(fpath, 'w') as f:
		f.write(str(slist))

def main():
	root_url = 'https://www.qiushibaike.com/8hr/page/'
	fpath = r'.main.txt'
	slist = []
	for i in range(0, 1):
		new_url = root_url + str(i)
		slist = html_parser(new_url)
		html_outputer(slist, fpath)

if __name__ == '__main__':
	main()