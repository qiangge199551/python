from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import re
import time
import random
from pyquery import PyQuery as pq
from config import *
import pymongo
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


# driver = webdriver.phantomjs(service_args=SERVICE_ARGS)
# driver.set_window_size(1400, 900)
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values': {'images': 2}}
options.add_experimental_option('prefs', prefs)
# options.set_headless(headless=True)
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


def first_page():
	print('searching...')
	try:
		driver.get('https://www.taobao.com')
		input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
		button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
		input.send_keys(KEYWORD)
		button.click()
		total_page = re.compile('\d+').search(
			wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total'))).text
		).group(0)
		get_product()
		return int(total_page)
	except TimeoutException:
		return first_page()	


def next_page(page_number):
	print('turning...', page_number)
	try:
		input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
		button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
		input.send_keys(page_number)
		button.click()
		get_product()
	except TimeoutError as e:
		next_page(page_number)


def get_product():
	wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
	html = driver.page_source
	doc = pq(html)
	items = doc('#mainsrp-itemlist .items .item').items()
	for item in items:
		product = {
			'image': item.find('.pic .img').attr('src'),
			'price': item.find('.price').text(),
			'deal': item.find('.deal-cnt').text()[:-3],
			'title': item.find('.title').text(),
			'shop': item.find('.shop').text(),
			'location': item.find('.shop').text(),
		}
		print(product)
		save_to_mongo(product)


def save_to_mongo(result):
	try:
		if db[MONGO_TABLE].insert(result):
				print('存储到MONGODB成功', '\n')
	except Exception:
		print('存储到MONGODB失败', '\n')


def main():
	try:
		total_page = first_page()
		for page_number in range(1, total_page):
			for num in range(1, 15):
				time.sleep(random.randint(1, 3))
			next_page(page_number)
	except Exception:
		print('ERRORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR')
	finally:
		driver.close()


if __name__ == '__main__':
	main()


