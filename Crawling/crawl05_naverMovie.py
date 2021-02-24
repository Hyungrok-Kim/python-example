# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json

html = requests.get('https://movie.naver.com/movie/running/current.nhn')
# print(html.text)
soup = BeautifulSoup(html.text, 'html.parser')

movies = soup.find('ul', {'class':'lst_detail_t1'})
#print(movies)



## 실습 1
# naverWebtoon.py 스크립트를 참조하여
# 영화 제목, 별점 정보를 사전 타입(자료형)으로 묶어
# 리스트를 만든 후
# movies.json 파일에 저장 하시오.

li = movies.select('li')

movieList = []
cnt = 0
for i in li:
    title = i.select_one('.tit a').text
    # text는 여러 개 값에 쓸 수 없고 find는 여러개를 가져오기 때문에
    # find로 가져오기 위해서는
    # title = i.find('.tit a')[0].text 이런 식으로 가져와야함.
    star = i.select_one('.info_star .star_t1 span.num').text
    book = i.select_one('.info_exp .star_t1.b_star span.num').text
    # 예매율이 기재되어있지 않은 영화들이 있기때문에 cnt로 상위 몇 개를
    # 뽑는다고 지정하지 않으면 에러가 남.

    tmp = {}
    tmp['title'] = title
    tmp['star'] = star
    tmp['book'] = book
    movieList.append(tmp)
    cnt += 1
    if cnt > 10:    # 상위 10개 뽑기
        break

result = {}
result['movie'] = movieList
result_json = json.dumps(result, ensure_ascii=False)

print(result_json)


with open('movie.json', 'w', encoding='utf-8') as myFile:
    myFile.write(result_json)