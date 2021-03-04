# -*- coding:utf-8 -*-

from pymongo import MongoClient
import pprint
# PrettyPrint

client = MongoClient('localhost', 27017)
db = client.test
score = db.score

aggr = score.aggregate([
    {
        '$match' : { 'mid.kor' : {'$gte' : 50 }}
    },
    {
        '$group': {
            '_id':'kor',
            'sum':{'$sum':'$mid.kor'}
        }

    }
])

print(aggr)

pprint.pprint(list(aggr))
