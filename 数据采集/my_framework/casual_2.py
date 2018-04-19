import asyncio
import aiohttp

async def main():
	fip =  ['114.215.174.227',
           '175.11.200.81',
           '117.127.0.199',
           '114.215.103.121',
           '39.104.28.240',
           '113.90.244.255',
           '39.134.10.19',
           '211.159.171.58',
           '123.134.250.189',
           '27.156.235.0']
	for item in fip:
		try:
			async with aiohttp.ClientSession( headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'},
			  conn_timeout=10) as session:
				async with session.get('https://www.baidu.com', proxy='http://'+item) as response:
					if response.status != 200:
						fip.remove(item)
		except:
			fip.remove(item)
			continue
	print(fip)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()