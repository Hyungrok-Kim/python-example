# -*- coding:utf-8 -*-
# 가져올 때 한글 깨지면 안되니까 하는 coding:utf-8

from pymongo import MongoClient
import pprint
# pprint -> 객체를 들여쓰기 형식으로 보기 좋게 뽑아주는 모듈
# mongo shell에서 find().pretty()하는 것과 비슷
'''
{'name:'hong', 'age':10} --> {
                                  'name' : 'hong',
                                  'age' : 10
                             }
'''

client = MongoClient('localhost', 27017)
db = client.test
score = db.score


cursor = score.find()
print(cursor)

for doc in cursor:
    pprint.pprint(doc)   # pprint가 키값 정렬도 해줌.

### 특정 문서만 찾기
gang = score.find({'name':'강호동'})
pprint.pprint(gang)

### 여러 개 나올 수도 있으니까
for doc in gang:
    pprint.pprint(doc)

### 한 명의 특정 문서만 찾기
a = score.find_one({'name':'dong'})
pprint.pprint(a)

print('document의 총 갯수 : ', score.count_documents({}))
# 조건 주기
# print('document의 총 갯수 : ', score.count_documents({'name':'gogil'}))

# 국어 점수가 40점 넘는 사람들만 뽑기
kor = score.find({'kor':{'$gt':50}})
for doc in kor:
    pprint.pprint(doc)