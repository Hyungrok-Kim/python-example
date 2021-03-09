from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
score = db.score

result01 = score.update_one(
    {
        'name' : '지미유'
    },
    {
        '$set': {'mid.kor': 95}
    }
)

print(result01.matched_count)  # 찾은 문서 갯수가 몇 개냐?
print(result01.modified_count) # 바뀐 문서 갯수가 몇 개냐?

result02 = score.update_many(
    {
        'mid.eng' : {'$lt': 80}
    },
    {
        '$set':{'mid.eng':100}
    }
)

print(result02.matched_count)
print(result02.modified_count)
