import re, trip

@trip.coroutine
def get_proxies(urls):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',}
	response = yield [trip.get(url, headers=headers) for url in urls]
	raise trip.Return(response)

@trip.coroutine
def test_proxies(response):
	print(response)
	proxies = []
	for res in response:
		proxy = re.findall(r'<td>(\d\.){1,3}(\d){1,3}</td>', res.text)
		proxies.append(proxy)
	print(proxies)
	for proxy in proxies:
		if trip.get('https://www.baidu.com', proxies={'http': proxy, 'https':proxy}, timeout=5):
			print('%s is valid' % proxy)
		else:
			continue
			
@trip.coroutine
def main():
	urls = ['http://www.xicidaili.com',]
	proxies = trip.run(get_proxies(urls))
	trip.run(test_proxies(proxies))
		
# if __name__ == '__main__':
# 	trip.run(main)


# import pymongo
# client = pymongo.MongoClient('localhost')
# db = client['ProxyPool']
# 	try:
# 		print(filter(lambda x: x, response))
# 		db['ip'].insert((filter(lambda x: x, response)))
# 	except:
# 		print('FAIL TO SAVE TO MONGODB ')