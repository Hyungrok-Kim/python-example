# -*- coding:utf-8 -*-

import pickle
'''
# 저장하는 방법
# pickling : 객체 -> 바이너리 파일
student = { 'name':'홍길동', 'age':15, 'gender':'M', 'addr':'서울시 강남구'}
with open('test02.txt', 'wb') as myFile: # 저장할거다. byte단위로 --> wb --> 그래서 text02의 문자가 꺠짐.
    pickle.dump(student, myFile)
'''
# 불러오는 방법
# unpickling : 파일 -> 객체 
with open('test02.txt', 'rb') as myFile :
    result = pickle.load(myFile)
    print(result)