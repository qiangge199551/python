import aiohttp
import asyncio
from fake_useragent import UserAgent
import re
import motor


async def parser(url):
	headers = {'User-Agent': UserAgent().random, }
	async with aiohttp.ClientSession(headers=headers) as session:
		try:
			async with session.get(url, headers=headers, timeout=10) as response:
				proxy = {str(response.url).split('.')[1]:re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', await response.text(), re.S)}
				# print(proxy, '\n\n\n')
				db = motor.MotorClient('localhost', 27017)['fip']['wait_for_verification']
				await db.insert_one(proxy)
		except:
			''

def main():
	url_list = ['http://www.xicidaili.com', 'https://www.kuaidaili.com/free/', 'http://ip.zdaye.com/', 'http://www.89ip.cn/tiqv.php?tqsl=30000',
	'https://proxy.mimvp.com/free.php?proxy=in_hp', 'http://www.coobobo.com/free-http-proxy', 'http://www.mayidaili.com/free/anonymous/%E9%AB%98%E5%8C%BF',
	 'http://http.taiyangruanjian.com/', 'http://http.zhimaruanjian.com/']
	loop = asyncio.get_event_loop()
	task = [parser(url) for url in url_list]
	loop.run_until_complete(asyncio.wait(task))
	loop.close()

if __name__ == '__main__':
	main()
