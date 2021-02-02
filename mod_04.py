# -*- coding:utf-8 -*-

import numpy as np   # 사용중이면 불들어옴
import matplotlib.pyplot as plt
import random

list01 = np.arange(15).reshape(3,5)
print(list01)

def plt01():
    x = np.arange(0,11)
    y = x

    print(x)

    plt.plot(x, y)

    # x축, y축 라인 이름
    plt.xlabel('x')
    plt.ylabel('y')

    # 범례
    plt.legend(['y=x'])

    plt.show()


def plt02():
    y = [random.randint(0, 10) for i in range(10)]
    x = range(10)

    print(y)

    plt.bar(x, y)

    # 축 간격 설정
    plt.xticks(range(11))
    plt.yticks(range(11))

    plt.show()


def plt03():
    data = [random.randint(100, 1000) for i in range(4)]
    plt.pie(data)

    category = ['first', 'second', 'third', 'fourth']
    plt.legend(category)

    plt.show()

# ---------------------

if __name__=='__main__':
    plt03()

