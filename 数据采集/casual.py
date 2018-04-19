import trip

@trip.coroutine
def main():
	global r
	r = yield trip.get('https://github.com/timeline.json')
trip.run(main)
print(r.text)