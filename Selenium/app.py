from selenium import webdriver
from time import sleep
import datetime as dt

driver = webdriver.Chrome()
driver.get('https://haktuts.blogspot.com/2018/09/coin-master-50-free-spin-and-coin-link.html?m=1')
element = driver.find_elements_by_css_selector("blockquote.tr_bq a")
title = []
link = []
for ele in element[0:10]:
    title.append(ele.get_attribute('text'))
    link.append(ele.get_attribute('href'))

date = dt.datetime.today().strftime('%d.%m.%Y')
# date = '02.06.2020'
for text, href in zip(title, link):
    txt = text.split(" ")
    if date in txt:
        print(f'<!-- wp:paragraph --> <p>{text} - <a href= "{href}">LINK</a> </p> <!-- /wp:paragraph -->')
