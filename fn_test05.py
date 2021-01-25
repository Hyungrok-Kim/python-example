# -*- coding:utf-8 -*-

def fibo1(n):
    a, b = 0, 1
    i = 0
    while i < n:
        print(a, end=" ")
        a, b = b, a+b
        i += 1
    print()

def fibo2(n):
    result = []
    a, b = 0, 1
    i = 0
    while i < n:
        result.append(a)
        a, b = b, a+b
        i += 1
    return result
# ----------------------------
if __name__=="__main__":
    n = int(input('n 입력 : '))
    fibo1(n)
    fiboResult = fibo2(n)
    print(fiboResult)



