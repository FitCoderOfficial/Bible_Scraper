from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import json
import os

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

bible_start = driver.find_elements_by_class_name('bookLink')[0].click()
time.sleep(1)

chapter_start = driver.find_elements_by_css_selector('#article > article > div > nav > div > ul.grid.chapters.clearfix > li')[0].click()
time.sleep(1)

# #현재 링크 확인
current_link = driver.current_url


# chapter_next = driver.find_elements_by_css_selector('#publicationNavigation > div > ul > li.resultNavRight')[0].click()
# chapter_next
# print(chapter_next)

#publicationNavigation > div.chrome.forwardBackNavControls.resultNavControls.meps-lang-KO.meps-script-KOREAN > ul > li.resultNavRight.disabled

# class chapter_save:
#     req = requests.get(current_link)
#     html = req.text
#     soup = BeautifulSoup(html, 'html.parser')
#     article_list = soup.select('article > p > span')
#     f = open('test{}.txt'.format(number), 'w', encoding='utf-8')
#     for i in article_list:
#         f.write(i.get_text()+'\n')
#     f.close()


class group_scraping:

    while True:
        number=1
        if driver.find_elements_by_css_selector('#publicationNavigation > div > ul > li.resultNavRight.disabled'):
            current_link = driver.current_url
            title = driver.find_elements_by_css_selector('#article > article > header > h1')[0].text.strip()
            req = requests.get(current_link)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            article_list = soup.select('article > p > span')
            f = open('{}{0}.txt'.format(title, number), 'w', encoding='utf-8')
            for i in article_list:
                f.write(i.get_text()+'\n')
            f.close()
            back_to_menu = driver.find_elements_by_css_selector('#menuBible')[0].click()
            number=1
            break
        else:
            current_link = driver.current_url
            title = driver.find_elements_by_css_selector('#article > article > header > h1')[0].text.strip()
            req = requests.get(current_link)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            article_list = soup.select('article > p > span')
            f = open('{}{0}.txt'.format(title, number), 'w', encoding='utf-8')
            for i in article_list:
                f.write(i.get_text()+'\n')
            f.close()
            number+=1
            go_to_next = driver.find_elements_by_css_selector('#publicationNavigation > div > ul > li.resultNavRight')[0].click()

group_scraping






