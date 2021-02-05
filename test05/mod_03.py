# File > settings > Project -> Project Interpreter에서
# + 버튼을 클릭해 numpy와 matplotlib (모듈)라이브러리를 install해준다.

# -*- coding:utf-8 -*-
import numpy as np
list01 = [i for i in range(0, 15)] # 0부터 14까지 list01에 배열이 만들어짐
print(list01)

np_arr01 = np.array(list01).reshape(3, 5)    # list를 row와 column이 있는 테이블 형태의 표 형식으로 바꿈(그래프를 만들기 위해서)
print(np_arr01)


