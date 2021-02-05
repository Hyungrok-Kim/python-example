# -*- coding:utf-8 -*-
# 파일 IO(입출력)
'''
파이썬 파일 권한
r : 파일 읽기 권한
w : 파일 쓰기 권한 (기존 내용 덮어쓰기)
a : 파일 쓰기 권한 (기존 내용에 덧붙이기, 추가하기)
x : 새로운 파일을 생성하여 쓰기 (이미 해당 파일이 있으면 ERROR) (execute)
t | b : text | binary파일을 문자로 읽을 것인지, byte로 읽을 것인지 선택
        (기본값은 't')
'''
"""
myFile = open('test01.txt', 'w')
myFile.write('Hello,Friday! Yeah!')
myFile.close()
"""

myFile = open('test01.txt', 'r')
str01 = myFile.read()
print(str01)
myFile.close()
# 항상 open해서 close해줘야함. 