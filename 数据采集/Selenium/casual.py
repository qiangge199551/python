from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

import time
import random
from tqdm import tqdm


for num in tqdm(range(200)):
	time.sleep(0.01)

browser = webdriver.Chrome()
try:
	for num in range(1, 15):
		ran = random.randint(1, 3)
		time.sleep(ran)
	browser.get('http://zhihu.com/explore')
	browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
	browser.execute_script('alert("To Bottom")')
	wait = WebDriverWait(broeser, 10)
	
finally:
	time.sleep(5)
	browser.close()




