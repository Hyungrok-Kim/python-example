
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017) #locolhost와 동일한 의미
db = client.test
score = db.score

result01 = score.delete_one({'name':'아기자기'})
print(result01.deleted_count)

result02 = score.delete_many({'mid.math':{'$lt': 100}})
print(result02.deleted_count)

# score.delete_many({}) # 컬렉션의 데이터 전부 삭제


