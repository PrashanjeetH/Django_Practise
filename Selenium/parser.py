import requests
from bs4 import BeautifulSoup
import re
page = requests.get("https://haktuts.blogspot.com/2018/09/coin-master-50-free-spin-and-coin-link.html?m=1")
soup = BeautifulSoup(page.content, features="html.parser")
links = soup.findAll("blockquote")
fp = open("scrapper.txt", "a")
for link in soup.findAll("blockquote"):
    fp.write(str(link))
    print(link)
fp.close()
# print(links)
