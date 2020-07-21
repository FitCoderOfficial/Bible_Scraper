from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import json
import os


req = requests.get('https://wol.jw.org/ko/wol/b/r8/lp-ko/nwtsty/1/1#study=discover')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
#article_list = soup.find('div', {'id':'article'})
#article_list = soup.findAll('span', {'class':'tt vl'})

article_list = soup.select('article > p > span')

f = open('test3.txt', 'w', encoding='utf-8')
for i in article_list:
    f.write(i.get_text()+'\n')

f.close()    

print(article_list)


# f = open('test3.txt', 'w', encoding='utf-8')

# for i in article_list:
#     f.write(i.get_text()+'\n')

# # for i in article_list:
# #     f.write(i.get_text())

# f.close()    


 
