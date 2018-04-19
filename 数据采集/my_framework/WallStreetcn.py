import sys
import re
from urllib.parse import urlencode
import requests
import pymongo
import datetime
import multiprocess as mp

category_map = {
	'1': '外汇',
	'2': '股市',
	'3': '商品',
	'4': '债市',
	'5': '央行',
	'6': '中国',
	'7': '美国',
	'8': '欧元区',
	'9': '日本',
	'10': '英国',
	'11': '澳洲',
	'12': '加拿大',
	'13': '瑞士',
	'14': '其他地区',
}

def num2name(category_num):
	if category_map.has_key(category_num):
		return category_map[category_num]
	else:
		return None

class mongodb(object):
	"""docstring for mongodb"""
	def __init__(self, host, port, name, password, databse, collection):
		self.host = host
		self.port = port
		self.name =name
		self.password = password
		self.databse = databse
		self.collection = collection
	def Connection(self):
		connection = pymongo.Connection(host = self.host, port=self.port)
		db = connection[self.database]
		if self.name or self.password:
			db.authenticate(name=self.name, password=self.password)
		posts = db[self.collection]
		return posts

def ResultSave(url,data):
	content = requests.get(url=url, params=params).content
	return content

def Spider(url, params):
	text = requests.get(url, params=params).text
	return text

def ContentSave(item):
	save_host = 'localhost'
	save_port = 27017
	save_name = ''
	save_password = ''
	save_database = 'textclassify'
	save_collection = 'wallstreetcn'
	source = 'wallstreetcn'
	createdtime = datetime.datetime.now()
	type = item[0]
	content = item[1].decode('unicode_escape')
	content = content.encode('utf-8')
	categorySet = item[2]
	category_num = categorySet.split(',')
	category_name = map(num2name, category_num)
	# districtset = set(category_name)&{'中国'，'美国', '欧元区', '日本', '英国', '澳洲', '加拿大', '瑞士', '其他地区'}
	districtset = set(category_name)&{u"中国", u"美国", u"欧元区", u"日本", u"英国", u"澳洲", u"加拿大", u"瑞士", u"其他地区"}
	district = ','.join(districtset)
	propertyset = set(category_name)&{'外汇', '股市', '商品', '债市'}
	property = ','.join(propertyset)
	centralbankset = set(category_name)&{'央行'}
	centralbank = ',',join(centralbankset)
	save_content = {
		'source': source,
		'createdtime': createdtime,
		'content': content,
		'type': type,
		'property': district,
		'centralbank': centralbank
	}
	ResultSave(save_host, save_port, save_name, save_password, save_database, save_collection, save_content)
def func(page):
	url = 'https://wallstreetcn.com/live/global'
	data = {
		'page': page
	}
	content = Spider(url, data)
	items = re.compile(r'"type:"(.*?)","codeType".*?"contentHtml":"(.*?)","data".*?"categorySet":"(.*?)","hasMore"', content)
	if len(items) == 0:
		print("The End Page:", page)
		data = urllib.urlencode(data)
		full_url = url + 'data'
		print(full_url)
		sys.exit(0)
	else:
		print('The Page:', page, 'Downloading...')
		for item in items:
			ContentSave(item)

if __name__ == '__main__':
	start = datetime.datetime.now()
	start_page = 1
	end_page = 30
	# 多进程
	pages = [i for i in range(start_page, end_page)]
	p = mp.Pool()
	p.map_async(func, pages)
	p.close()
	p.join()
	# 单进程
	page = end_page

	while 1 :
		url = 'https://wallstreetcn.com/live/global'
		data = {
			'page': page
		}
		text = Spider(url, data)
		items = re.findall(r'"type":(.*?)","codeType".*?"contentHtml":"(.*?)","data".*?"categprySet":"(.*?)","hasMore"', text)
		if len(items) == 0:
			print('The End Page:', page)
			data = urlencode(data)
			full_url = url + data
			print(full_url)
			break
		else:
			print("The Page:", page, 'Downloading')
			for item in items:
				ContentSave(item)
			page += 1

		end = datetime.datetime.now()
		print('last time:', end-start)



