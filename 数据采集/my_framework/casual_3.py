import motor
import asyncio
import pprint
import aiohttp

async def main():
	db = motor.MotorClient('localhost', 27017)['fip']['wait_for_verification']
	for document in await db.find().to_list(length=10):
		del document['_id']
		pprint.pprint(document)
		for key, vaule in document.items():
			for item in vaule:
				try:
					async with aiohttp.ClientSession( headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'},
					  conn_timeout=10) as session:
						async with session.get('https://www.baidu.com', proxy={'https': 'https://'+item, 'http': 'http://'+item}) as response:
							if response.status != 200:
								document[key].remove(item)
				except:
					document[key].remove(item)
					continue
		pprint.pprint(document)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()