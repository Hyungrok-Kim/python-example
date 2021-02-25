# -*- coding:utf-8 -*-

from pymongo import MongoClient

#mongoDB주소로 연결
client = MongoClient('localhost', 27017)

#test라는 데이터베이스 연결
db = client.test

#Collection 연결
score = db.score

result01 = score.insert_many([
    {
        'name':'지미유',
        'mid':{'kor' : 100, 'eng' : 100, 'math' : 80},
        'final':{'kor' : 90, 'eng' : 90, 'math' : 85}
    },
    {
        'name':'아기자기',
        'mid':{'kor' : 50, 'eng' : 40, 'math' : 100},
        'final':{'kor' : 80, 'eng' : 85, 'math' : 95}
    }
])

print(result01.inserted_ids) # 추가되어진 아이들을 id로 뽑아줌
                             # mongoDB Shell에서 나오는 것처럼
result02 = db.score.insert_one(
    {
        'name':'강호동',
        'kor':90,
        'eng':50,
        'math':60
    }
)

print(result02.inserted_id)  # 추가되어진 아이를 id로 뽑아줌


