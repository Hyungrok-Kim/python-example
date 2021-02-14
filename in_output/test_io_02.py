# -*- coding:utf-8 -*-

# with 구문을 사용하면 자바의 try - with - resource 처럼
# close()를 생략할 수 있다!
with open('test01.txt', 'r') as myFile:  # with문으로 열면 close를 자동으로 해줌.
    str01 = myFile.read()
    print(str01)



