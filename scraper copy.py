from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import json
import os
import csv

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('D:\Works\PG_Works\Bible_Scraper\chromedriver')
# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)



# url에 접근한다.
driver.get('https://wol.jw.org/ko/wol/b/r8/lp-ko/nwt/1/1#study=discover')
#driver.get('https://wol.jw.org/en')



# #현재 링크 확인
current_link = driver.current_url


req = requests.get(current_link)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

article_list = soup.select('article > p > span')
chapter = driver.find_elements_by_css_selector('#article > article > header > h1')[0].text.strip()
title = driver.find_elements_by_css_selector('#article > article > header > h1')[0].text.strip()
number=1
f = open('{}{}.txt'.format(title, number), 'w', encoding='utf-8')
for i in article_list:
    temp = []
    temp.append(title)
    temp.append(str(number))
    temp.append(i.get_text())
    join_f = (join(temp))
    f.write('\n'.join(join_f))
f.close()

