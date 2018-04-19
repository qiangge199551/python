from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
import pymongo
from config import *
from pyquery import PyQuery as pq

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.maximize_window()
wait = WebDriverWait(browser, 10)
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def index_page(page):
	print('正在爬取第', page, '页')
	try:
		url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
		browser.get(url)
		if page>1:
			input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
			submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.main > span.btn.J_Submit')))
			input.clear()
			input.send_keys(page)
			submit.click()
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager li.item,active > span'), str(page)))
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
		get_products()
	except TimeoutException:
		index_page(page)

		
def get_products():
	save_to_mongo(product)


def save_to_monge(result):
	try:
		if bd[MONGO_COLLECTION].insert(result):
			print('存储到MongoDB成功')
	except Exception:
		print('存储到MongoDB失败')


def main():
	for i in range(1, MAX_PAGE + 1):
		index_page(i)
	browser.close()


if __name__ == '__main__':
	main()


