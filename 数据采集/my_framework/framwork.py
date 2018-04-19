import requests
from bs4 import BeautifulSoup
import re
import traceback
import json


class requests_():
	def get_url_text(url, encoding='utf-8'):
		try:
			headers = {
				'Cookie': '',
				'Host': '',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
			}
			proxies ={}
			session = requests.Session()
			response = session.get(url, auth = ('username', 'password'), headers=headers, proxies=proxies, timeout=30)
			response.raise_for_status()
			# print(response.status_code, response.request.headers, response.encoding, response.apparent_encoding)
			response.encoding = encoding
			return response
		except:
			print('get_stock_list ERROR')

	def get_stock_list(url, stock_list):
		response = get_url_text(url)
		re_stock_name = re.compile(r'[s][hz]\d{6}')
		for a in soup.find_all('a', href=re_stock_name):
			try:
				stock_list.append(re.findall(re_stock_name, str(a))[0])
			except:
				continue
		# for i in range(len(stock_list)):
		# 	if stock_list[i] == None:
		# 		del stock_list[i]
		return stock_list

	def get_stock_info(stock_list, fpath):
		url_baidu_stock = r'https://gupiao.baidu.com/stock/'
		stock = {}
		for i in range(100, 200):
			try:
				url_stock_price = url_baidu_stock + str(stock_list[i])
				soup = get_url_text(url_stock_price)
				price = soup.find('strong', attrs={'class': '_close'}).string
				stock[stock_list[i]] = price
			except:
				continue
		with open(fpath, 'a', encoding='utf-8') as f:
				f.write(str(stock))

	def main():
		url_eastmoney = r'http://quote.eastmoney.com/stocklist.html'
		stock_list = []
		fpath = r'E:\python\scrapy\stock\stock.txt'
		get_stock_list(url_eastmoney, stock_list)
		# print(stock_list[100:200])
		# with open(fpath, 'w') as f:
		# 	f.write(str(stock_list))
		# for i in range(len(stock_list)):
		# 	if re.match(re_stock_name, stock_list[i]) == 'None':
		# 		del(stock_list[i])
		get_stock_info(stock_list, fpath)

	if __name__ == '__main__':
		main()


import urllib
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
 
class urlib_():
	def get_html_text(url):


		# 设置代理
		proxy_handler = ProxyHandler({
		    'http': 'http://127.0.0.1:9743',
		    'https': 'https://127.0.0.1:9743'
		})
		opener = build_opener(proxy_handler)
		try:
		    response = opener.open('https://www.baidu.com')
		    print(response.read().decode('utf-8'))
		except URLError as e:
		    print(e.reason)


		try:
			url = 'http://httpbin.org/post'
			headers = {
				'User-Agent': r'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
				'Host': 'httpbin.org'
			}
			data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
			request = urllib.request.Request(url, data=date, headers=headers, timeout=10, method='POST')
			response = urllib.request.urlopen(request)
			response = urllib.request.urlopen(url, data=data, timeout=10)
			# print(response.read())
			# print(response.read().decode('utf-8'))
			# print(response.status)
			# print(response.getheaders())
			# print(response.getheader('Server'))
		except urllib.error.HTTPError as e:
		    print(e.reason, e.code, e.headers, sep='\n')
		except urllib.error.URLError as e:
		    print(e.reason)
		else:
		    print('Request Successfully')


