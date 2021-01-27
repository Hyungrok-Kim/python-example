# -*- coding:utf-8 -*-

# 1. for 반복문을 사용하여 구구단을 출력하는 함수 gugu()를 만들어 보세요
# 2. while 반복문을 사용하여 구구단 중 사용자가 입력한 단을 출력하는 gugudan(x)를 만들어 보세요.
# main함수 실행 시 해당 함수들이 순서대로 동작하도록 코드를 작성하세요
# 사용자의 입력은 input()함수를 사용하세요

def gugu():
    for i in range(2,10):
        print('<<--{}단-->>'.format(i))
        for j in range(1, 10):
            print('{} * {} = {}'.format(i, j , (i*j)))

def gugudan(x):
    print('<<--{}단-->>'.format(x))
    j = 1
    while j < 10:
        print('{} * {} = {}'.format(x, j, (x*j)))
        j += 1

if __name__ == '__main__' :
    gugu()
    x = int(input('무슨 단? :'))
    gugudan(x)
    
