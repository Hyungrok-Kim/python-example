
from pymongo import MongoClient

# 몽고DB를 연결하기 위해서 주소를 알아야 함.
# 몽고 Compass에 들어가면 HOST localhost:27017이라고 나와 있음.

# 파이썬 - 몽고DB 연결 객체 설정
client = MongoClient('localhost', 27017)
# DB 설정
db = client['test']
# db = client.test    --> 와 같이도 접근 가능

# Collection 설정
score = db['score']
# score = db.score    --> 와 같이도 접근 가능

# colleciton 내의 문서 결과 조회
result = score.find()

for bson in result:
    print(bson)


'''
db.score.insert_one({'name':'gogil', 'kor':100, 'eng':70, 'math':40})
db.score.insert_one({'name':'dong', 'kor':60, 'eng':90, 'math':70})
'''