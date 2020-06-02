from selenium import webdriver
from time import sleep
import datetime as dt
"""
driver = webdriver.Chrome()
driver.get('https://haktuts.blogspot.com/2018/09/coin-master-50-free-spin-and-coin-link.html?m=1')
element = driver.find_element_by_css_selector("blockquote.tr_bq a")
text = element.get_attribute('text')
link = element.get_attribute('href')
print(f"text = {text} || link = {link}")"""
text = "Coin master coins link 01.06.2020"
date = dt.datetime.today().strftime('%d.%m.%Y')
txt = text.split(" ")
print (txt)
print(date)
if date in txt:
    print("successfull!")
