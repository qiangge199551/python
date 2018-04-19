from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from pyquery import PyQuery as pq
import time

options = webdriver.ChromeOptions()
prefs = {'profile.defaule_content_setting_values': {'images': 1}}
options.add_experimental_option('prefs', prefs)
options.set_headless(headless=False)
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

def get_html(url):
	print('searching....')
	try:
		driver.get(url)
		input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#kw')))
		button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#su')))
		input.send_keys('种子搜索网站')
		button.click()
		time.sleep(2)
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		print(driver.page_source)
		return driver.page_source
	except TimeoutException:
		get_html(url)
	finally:
		driver.close()

def main():
	url = 'http://www.12306.cn/mormhweb/'
	html = get_html(url)


if __name__ == '__main__':
	main()



