# number : 숫자 자료형

# 정수형
a = 100
print(a)
# a가 어떤 타입인지
print(type(a)) # <class 'int'>

# 정수형 계산
print(int(9.8)) # 9 : 소수점 이하는 버린다!
print(7/6)      # 자바에서는 7/6을 하면 몫만 남고
                # 끝나는데 파이썬은 정수형 계산 시
                # 소수점까지 계산해 줌
                # 정수형 계산 시 / 결과가 실수로 나온다!
# 몫만 구하고 싶을 때
# print(int(7/6))
print(type(int('5'))) # <class 'int'> ==> java에서 Integer.parseInt() 메소드와 같음
#print(type(int('5점'))) # 에러뜸 5점이라는 문자열은 int로 바꿀 수 없다.

# 자바에서 실수형은 float 과 double
# 파이썬은 float밖에 없음
# 실수형
b = 100.1
print(b)
print(type(b)) # <class 'float'>

# 실수형 계산
print(float(5))    # float(정수) ==> 실수형으로 형변환이 발생한다.
print(float(3 + 2)) # 정수형 계산 시 '/' 연산을 제외한 +, -, * 연산은 그 결과가 정수형으로
                    # 나오기 때문에 실수를 만들고 싶으면 float()
print(type(float('1.5'))) # <class 'float'>

# 2진수(b:binary), 8진수(o:octal) 16진수(x:hexa)
c, d, e = 0b1011, 0o77, 0xff
print(c)
print(d)
print(e)









