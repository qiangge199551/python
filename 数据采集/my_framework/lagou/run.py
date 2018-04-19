from multiprocessing import Pool
import threading
import pymongo
from crawler import *
from config import *


def main():
	# thread_one = threading.Thread(target=start, args=(3,))
	# thread_one.start()
	# thread_two = threading.Thread(target=start, args=(2,))
	# thread_two.start()
	# thread_one.join()
	# thread_two.join()
	with Pool() as pool:
		pool.map(start, range(first_page, total_page))


if __name__ == '__main__':
	main()