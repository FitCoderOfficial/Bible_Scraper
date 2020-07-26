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
driver.get('https://wol.jw.org/ko')
#driver.get('https://wol.jw.org/en')

# # id="menuPublications" 인 값을 찾는다
element = driver.find_element_by_id("menuPublications").click()
time.sleep(1)

# # 리스트 값중에 첫번째 값을 찾는다
Publications_list = driver.find_elements_by_css_selector('#article > article > div > nav > ul > li')[0].click()
time.sleep(1)


bible_list = driver.find_elements_by_css_selector('#article > article > div > nav > ul > li')[0].click()
time.sleep(1)

def book_loop():
    book_list = range(len(driver.find_elements_by_class_name('bookLink')))
    for i in book_list:
        bible_start = driver.find_elements_by_class_name('bookLink')[i].click()
        chapter_start = driver.find_elements_by_css_selector('#article > article > div > nav > div > ul.grid.chapters.clearfix > li')[0].click()
        group_scraping()
        time.sleep(3)

def group_scraping():
    while True:
        if driver.find_elements_by_css_selector('#publicationNavigation > div > ul > li.resultNavRight.disabled'):
            verse_scraping()
            back_to_menu = driver.find_elements_by_css_selector('#menuBible')[0].click()
            
            break
        else:
            verse_scraping()
            go_to_next = driver.find_elements_by_css_selector('#publicationNavigation > div > ul > li.resultNavRight')[0].click()

def verse_scraping():
    #현재 링크 확인
    current_link = driver.current_url

    req = requests.get(current_link)
    html = req.text 
    soup = BeautifulSoup(html, 'html.parser')
    title = driver.find_elements_by_css_selector('#article > article > header > h1')[0].text.strip()
    chapter = soup.select('a.cl > strong')[0].get_text()
    article_list = soup.select('article > p > span')

    f = open('{}{}.csv'.format(title, chapter), 'w', encoding='utf-8-sig', newline='')
    for i in article_list:
        verse = article_list.index(i)+1
        temp = []
        if article_list.index(i) == 0:
            data_list = temp + ([title, chapter, verse, i.get_text().replace('+', '').replace('*', '')[len(str(chapter)):]])
        else:
            data_list = temp + ([title, chapter, verse, i.get_text().replace('+', '').replace('*', '')[len(str(verse)):]])
        wr = csv.writer(f)
        wr.writerow(data_list)
    f.close()


book_loop()