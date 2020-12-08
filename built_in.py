# Built in 함수
# 자바의 Integer, String 클래스처럼
# 특정 값을 특정 자료형으로 바꿔주는 내장 함수들

# int() : 정수
print(int(True))
print(int(False))
print(int(123.45))
print(int('100'))

# float() : 실수
print(float(3.3))
print(float('3'))
print(float(True))

# str() : 문자열
print(str('Hello world'))
print(type(str('Hello World!')))

# repr() : '문자열' 객체   # 문자열이라는 객체 그 자체를 보여주기 때문에 ''가 붙어서 나옴
print(repr('Hello world!')) # 컴퓨터에게 값으로 인식시킬 것이냐, Object로 인식시킬 것이냐
print(type(repr('Hello World!')))

# help(str)  # 자바의 라이브러리 문서와 같이 파이썬은 help문으로 알아낼 수 있음
             # 파이썬도 document 문서 찾을 수 있음 파이썬 홈페이지에서
# help(repr)

