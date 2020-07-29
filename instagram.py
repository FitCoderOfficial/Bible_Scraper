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
driver.get('https://www.instagram.com/udtbro')
#driver.get('https://wol.jw.org/en')



# #현재 링크 확인
current_link = driver.current_url


req = requests.get(current_link)
r = req.text 
soup = BeautifulSoup(r, 'html.parser')

# follower = soup.select('meta', {'name': 'description'})['content']
# for i in follower:
#     print(i.get_text())
# print (follower)

start = '"edge_followed_by":{"count":'
end = '},"followed_by_viewer"'
followers= r[r.find(start)+len(start):r.rfind(end)]

start = '"edge_follow":{"count":'
end = '},"follows_viewer"'
following= r[r.find(start)+len(start):r.rfind(end)]

print(followers, following)


