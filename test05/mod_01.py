# -*- coding:utf-8 -*-

# 1. import 모듈명(.py이름) [as 별칭] # 모듈이름이 너무 길 때 별칭 부여가 가능함.
# 2. from 모듈명 import 함수|변수명

# import math as ms
# math 모듈(즉 Library)를 가져온다.

from math import pi
# math 모듈에서 pi만 가져올거다! 변수명을 바로 쓸 수 있게 됨. 앞에 math.을 하지 않아도

def circle(r): # 반지름을 받아서 원의 넓이를 구하는 함수
    return r * r * pi

# -------------------------------------------

if __name__=='__main__':
    print('PI : ', pi)   # 파이를 외부 모듈로서 가져오는 경우
    radius = int(input('원의 반지름 :'))
    print('원의 반지름은 {}이며, 원의 넓이는 {:.2f}입니다.'.format(radius, circle(radius)))


