# -*- encoding:utf-8 -*-

root_url = 'http://hz.58.com/chuzu/?PGTID=0d200001-0004-feb5-2a65-0561bc10aacf&ClickID=1'

from bs4 import BeautifulSoup
import requests
import sys

response = requests.get(root_url)
response.encoding = 'utf-8'
# print(response.status_code)
soup = BeautifulSoup(response.text, 'lxml')
# soup = soup.prettify()
# print(soup)
titles = soup.select('body > div.mainbox > div.main > div.content > div.listBox > ul > li > div.des > h2 > a')
rooms = soup.select('body > div.mainbox > div.main > div.content > div.listBox > ul > li > div.des > p.room')
locations = soup.select('body > div.mainbox > div.main > div.content > div.listBox > ul > li > div.des > p.add')
prices = soup.select('body > div.mainbox > div.main > div.content > div.listBox > ul > li > div.listliright > div.money > b')


for (title, room, location, price) in zip(titles, rooms, locations, prices):
	data = {
	'title': title.get_text(),
	'room': room.get_text(),
	'location': location.get_text(),
	'price': price.get_text(),
	}
	with open('output.html', 'w') as f:
		f.write(str(data))


