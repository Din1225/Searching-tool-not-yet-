from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import base64
import requests
from selenium.webdriver.common.keys import Keys

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

#手動打
time.sleep(3)
ocr = input("請輸入驗證碼:")
element = browser.find_element("name","auth_num")
element.send_keys(ocr)
element.send_keys('\ue007')

# #定位驗證碼圖片
# img_base64 = browser.execute_script("""
#     var ele = arguments[0];
#     var cnv = document.createElement('canvas');
#     cnv.width = ele.width; cnv.height = ele.height;
#     cnv.getContext('2d').drawImage(ele, 0, 0);
#     return cnv.toDataURL('image/jpeg').substring(22);    
#     """, browser.find_element("xpath","/html/body/div/form/table[2]/tbody/tr/td/img"))

# with open("captcha_login.png", 'wb') as image:
#     image.write(base64.b64decode(img_base64))
# file = {'file': open('captcha_login.png', 'rb')}  #下載下來的一般驗證碼(Normal Captcha)圖片

# time.sleep(3)
# #解碼
# from PIL import Image
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# img = Image.open(r"C:\Users\ASUS\Documents\github-project\Searching-tool\captcha_login.png")
# img = img.convert("L")
# ans = pytesseract.image_to_string(img)
# time.sleep(5)
# print(ans)


# import tkinter as tk
# root = tk.Tk()


time.sleep(10)
browser.quit()