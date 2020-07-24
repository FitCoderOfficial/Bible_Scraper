from selenium import webdriver
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
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
driver.get('https://wol.jw.org/ko/wol/b/r8/lp-ko/nwt/1/20#study=discover')
#driver.get('https://wol.jw.org/en')



# #현재 링크 확인
current_link = driver.current_url



#배열
# data_list =[] 
# column_names = ['title', 'chapter', 'verse', 'detail']



def verse_scraping():
    req = requests.get(current_link)
    html = req.text 
    soup = BeautifulSoup(html, 'html.parser')
    title = driver.find_elements_by_css_selector('#article > article > header > h1')[0].text.strip()
    chapter = soup.select('a.cl > strong')[0].get_text()
    print(chapter)
    article_list = soup.select('article > p > span')


    f = open('{}{}.csv'.format(title, chapter), 'w', encoding='utf-8-sig', newline='')
    for i in article_list:
        verse = article_list.index(i)+1
        temp = []
        if article_list.index(i) == 0:
            data_list = temp + ([title, chapter, verse, i.get_text()[len(str(chapter)):]])
        else:
            data_list = temp + ([title, chapter, verse, i.get_text()[len(str(verse)):]])
        wr = csv.writer(f)
        wr.writerow(data_list)
    f.close()

verse_scraping()

        


