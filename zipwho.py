from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from shutil import which
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from basic import sheet_length,zip_code,county,city

chrome_path = which('chromedriver.exe')
chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("start-maximized")


driver = webdriver.Chrome(executable_path = chrome_path,options=chrome_options)

driver.get("http://zipwho.com/")
time.sleep(5)
l = sheet_length()
for k in range(l+1):
    city_= city(k)
    zip_ = zip_code(k)
    county_ = county(k)
    




# driver.quit()
