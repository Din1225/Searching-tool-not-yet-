from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/6/6.2/6.2.9/JH629001.php")

time.sleep(5)

#找到開課代號的選單
select_department = Select(browser.find_element("name","cou_code"))
#找到GE並點擊
want = re.compile("GE")
for department in select_department.options:
    value = department.get_attribute('value')
    if want.search(value):
        department.click()
        break

#定位驗證碼圖片



time.sleep(10)
browser.quit()