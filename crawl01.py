import requests

# import bs4
# bs4는 requests로 불러온 모든 데이터에서 필요한 데이터만 목적에 맞게 추출하는 역할을 함.

html = requests.get('https://ko.wikipedia.org/wiki/%EB%9D%BC%EB%A9%B4')

print(html.text)