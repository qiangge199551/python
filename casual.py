import asyncio

async def do_some_work(x):
	await asyncio.sleep(x)
	print("Waiting " + str(x))

loop = asyncio.get_event_loop()
tasks = [do_some_work(3) for i in range(10)]
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()