# -*- coding:utf-8 -*-

def func01(x, y):
    return x + y

def func02(x, y):
    return x + y, x - y   # 이런 식으로 반환을 두 개 할 수 도 있음.

def func03(x,y):
    print("{} * {} = {}".format(x,y,(x*y)))
#########

if __name__ == '__main__':
    a = func01(10, 5)
    print(a)
    b = func02(10, 5)
    print(b)
    print(type(b))
    # 만약 결과를 여러 개 전달하면
    # tuple(튜플)의 형태로 묶어서 하나의 객체를 반환한다.
    num1, num2 = func02(20, 4)
    print(num1, num2)
    func03(10,5)