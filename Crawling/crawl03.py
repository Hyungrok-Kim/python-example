import requests
from bs4 import BeautifulSoup

html = requests.get('https://news.daum.net/digital')
soup = BeautifulSoup(html.text, 'html.parser')
#result = soup.select('.tit_thumb > a')             ## select / select_one : 선택자로 태그 가져오기
result = soup.find_all('a', class_='link_txt')      ## find_all / find : 태그의 속성을 직접 명시하여 가져오기
for i in result:
    #print(i)
    print(i.text) # link_txt라는 클래스를 가진 a태그의 글자만 가져오는 방법

print('--------')
print(result) # 이렇게 뽑으면 맨 앞에 것만 뽑게 됨. a태그가 많기 때문에

