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
driver.get('https://wol.jw.org/ko/wol/b/r8/lp-ko/nwt/1/50#study=discover')
#driver.get('https://wol.jw.org/en')



# #현재 링크 확인
current_link = driver.current_url

# req = requests.get('https://wol.jw.org/ko/wol/b/r8/lp-ko/nwtsty/1/50#study=discover')
# html = req.text
# soup = BeautifulSoup(html, 'html.parser')
#article_list = soup.find('div', {'id':'article'})
#article_list = soup.findAll('span', {'class':'tt vl'})



# class chapter_scraper:
#     article_list = soup.select('article > p > span')
#     f = open('test4.txt', 'w', encoding='utf-8')
#     for i in article_list:
#         f.write(i.get_text()+'\n')
#     f.close()


# chapter_scraper


# f = open('test3.txt', 'w', encoding='utf-8')

# for i in article_list:
#     f.write(i.get_text()+'\n')

# # for i in article_list:
# #     f.write(i.get_text())

# f.close()    


 
# class group_scraping:
#     while True:
#         if driver.find_elements_by_css_selector('#publicationNavigation > div > ul > li.resultNavRight.disabled'):
#             back_to_menu = driver.find_elements_by_css_selector('#menuBible')[0].click()
#             break
#         else:
#             go_to_next = driver.find_elements_by_css_selector('#publicationNavigation > div > ul > li.resultNavRight')[0].click()

# group_scraping


title = driver.find_elements_by_css_selector('#article > article > header > h1')[0].get_text()
print(title)