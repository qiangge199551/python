import requests
from bs4 import BeautifulSoup
import bs4

def get_url_text(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		print(r.ststus_code)
		return ''

def fill_university_list(ulist, html):
	soup = BeautifulSoup(html, 'html.parser')
	for tr in soup.find('tbody').children:
		if isinstance(tr, bs4.element.Tag):
			tds = tr('td')
			ulist.append([tds[0].string, tds[1].string, tds[3].string])

def print_university_list(ulist, num):
	tplt = '{0:^10}\t{1:{3}^10}\t{2:^10}'
	print(tplt.format('排名','学校名称','总分', chr(12288)))
	for i in range(num):
		u = ulist[i]
		print(tplt.format(u[0], u[1], u[2], chr(12288)))	

def main():
	url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
	html = get_url_text(url)
	unifo = []
	fill_university_list(unifo, html)
	print_university_list(unifo, 20) # 20 universities


if __name__ == '__main__':
	main()