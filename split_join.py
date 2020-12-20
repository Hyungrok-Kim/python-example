# 정규표현식 관련 모듈(라이브러리) 추가하기
import re

# 문자열 관련 함수
# split : 문자열을 특정 구분자로 쪼개는 함수
str01 = 'Hello, World!\nHello, Python!'
print(str01)
arr01 = str01.split(' ')   # 문자열을 쪼개면 배열이 나오니까 띄워쓰기 단위로 쪼개서
                           # 배열에 담음
print(arr01)

# join : 쪼개진 / 여러 문자열을 특정 구분자로 하나의 문자열을 만드는 함수
arr02 = ['1', '2', '3', '4']
print(arr02)
print('+'.join(arr02)) # 구분자를 앞에 쓰고 join 쓰고 배열! 자바와 순서가 다름

# eval : 특정 코드 형태로 짜여진 문자열을 실제 코드로 읽어주는 함수
str02 = '+'.join(arr02)
print(eval(str02))     # 이런 식으로 문자열을 실제 코드로 바꿀 수 있음.

# 실습 1
# date01 = ['2020', '12', '09' ] 리스트를
# 연, 월, 일 형태로 표현하고자 한다.
# 다음 출력문을 join 함수를 사용하여 표현 하세요.
# 'yyyy-mm-dd' 형태로 뽑아 보기
# [출력] : 2020-12-09
date01 = ['2020', '12', '09']
str03 = '-'.join(date01)
print(str03)

# 정규표현식 + split 맛보기 ( 정규표현식을 쓰려면 위에서 import re를 해줘야함 )

arr03 = re.split('[\s]|[,]', str01)
print(arr03)
