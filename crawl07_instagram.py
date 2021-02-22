# -*- coding:utf-8 -*-
'''

# 웹 브라우저 직접 접근이 아닌 파이썬을 통한 접근으로
# instagram에서 연결을 거부하는 현상이 있을 수 있다.
# 웹 테스트 도구인 셀레니움을 사용해서 문제점을 해결한다.


import requests
from bs4 import BeautifulSoup

tag = input('search tag : ')
url = 'https://www.instagram.com/explore/tags/' + tag

# 인스타그램에 직접적으로 접근하는 것이 아니라 파이썬을 거쳐 접근하기 때문에
# page Not Found 에러가 생길 수 있다.
# 그 문제점을 해결하기 위해 셀레니움 모듈을 쓴다.
# 셀레니움은 웹 페이지에 직접적으로 접근해줌.

# print(url)

result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

print(soup.text)
'''

from selenium import webdriver
from bs4 import BeautifulSoup
# 웹 드라이버를 다운받아야함. 웹 드라이버는 웹 브라우저마다 다 다름

url = 'https://www.instagram.com/explore/tags/' + input('검색할 태그 입력 : ')
#driver = webdriver.Chrome('C:\workspace\chromedriver_win32\chromedriver.exe')
 # 오라클 드라이버 사용하듯이 webdriver 사용

## 웹 브라우저를 켜지 않은 상태로 정보를 가져오는 설정
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')

driver = webdriver.Chrome('C:/workspace/chromedriver_win32/chromedriver.exe', options=options)

driver.implicitly_wait(5)  # 드라이버가 로딩되는 동안의 대기 시간을 초단위로 설정
driver.get(url)            # 웹 드라이버(웹 부라우저 역할)로 해당 url 간접

soup = BeautifulSoup(driver.page_source, 'html.parser')
imgList = soup.findAll('div', {'class', 'KL4Bh'})
# find와 select는 사용자의 취향차이 이다.
print(imgList)



