# Crow Taobao Price
import requests
from bs4 import BeautifulSoup
import re

def get_url_content(url):
	try:
		response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
		response.raise_for_status()
		print(response.status_code, response.encoding, response.apparent_encoding)
		print(response.request.headers)
		response.encoding = response.apparent_encoding
		return response
	except:
		print('get_url_content_ERROR')
		return 

def Parser(response,infolist):
	try:
		price_list = re.findall(r'"view_price":"[\d.]*"', response)
		# print(price_list)
		title_list = re.findall(r'"raw_title":".*?"',response)
		for i in range(len(price_list)):
			price = eval(price_list[i].split(':')[1])
			title = eval(title_list[i].split(':')[1])
			infolist.append([price,title])
	except:
		print('Parser_ERROR')
	return infolist

def Outputer(infolist):
	title_price_lit = '{:4}\t{:8}\t{:16}'
	print(title_price_lit.format('序号','商品价格','商品名称'))
	for i in infolist:
		count += 1
		print(title_price_lit.format(count, i[0], i[1]))
	pass

def main():
	url = 'https://s.taobao.com/search?q='
	GOODS = '书包'
	depth = 1
	start_url = r'https://www.taobao.com/search?q=' + GOODS
	infolist = []
	for i in range(depth):
		try:
			url = start_url
			print(url)
			response = get_url_content(url)
			infolist = Parser(response, infolist)
		except:
			continue
		Outputer(infolist)

if __name__ == '__main__':
	main()