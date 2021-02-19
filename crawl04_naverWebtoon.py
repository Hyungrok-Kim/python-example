# -*- coding:utf-8 -*-
# 6번째 줄이 문자열을 byte단위로 보낼 수 있기 때문에 맞춰주는 utf-8 방식

import requests
from bs4 import BeautifulSoup

import json
# 파이썬으로 json 객체를 다루기 위한 모듈

html = requests.get('https://comic.naver.com/webtoon/weekdayList.nhn?week=tue') # tue를 빼면 그날 그날 당일 웹툰으로 가져옴
soup = BeautifulSoup(html.text, 'html.parser') # html 받아와서 soup 객체 생성
# BeautifulSoup가 파일을 읽어올 때 xml인지 html인지 구분하기 위해서 'html.parser'를 사용한다.
# xml문서라면 'xml'


webtoons = soup.find('ul', class_='img_list') #파이썬의 클래스와 혼동할 수 있기 때문에 클래스를 구분하기 위해 _ 사용
#webtoons = soup.find('ul', {'class':'img_list'}) 도 잘 읽음
print(webtoons)
dl = webtoons.select('dl')
#print(dl)

webtoonList = []
for i in dl:
    title = i.find('a').text
    star = i.find('strong').text

    tmp = {}    # title과 star을 딕셔너리 형태로 보기 위한 임시 딕셔너리
    tmp['title'] = title
    tmp['star'] = star
    # print(tmp)
    webtoonList.append(tmp)

result = {}
result['webtoon'] = webtoonList # webtoon이라는 키 값에 webtoonList를 value로 담겠다.

result_json = json.dumps(result, ensure_ascii=False)   #dump는 담아주는것, dumps는 통으로 담는 것
                                # ascii코드로 담지 않겠다. default는 ascii이기 때문에 한글이 깨질 위험이 있다.
                                # 즉 한글이 담겨있으니 한글이 깨지지 않게 해주세요.
#print(result_json)

with open('webtoon.json', 'w', encoding='utf=8') as myFile: # 한글이 깨지지 않도록 encoding을 utf-8로 맞춰주세요.
    myFile.write(result_json)   # webtoon.json이라는 파일이 생기면서 result_json의 값이 들어감.
