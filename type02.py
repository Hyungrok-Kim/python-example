# 문자 자료형
# ', " 의 차이 없음

# 단일 따옴표 1개
a = 'python\n\'Hello world!\'' #\를 쓰면 문자열안에 ' 삽입 가능
print(a)

'''
    여러줄 주석 
'''

# 단일 따옴표 3개
b = ''' python's
        Hello World!
        Hello, python !!!  !!  !  
    '''
print(b) # 여러줄 문자열 작성이 가능하다!

# 쌍 따옴표 1개
c = "Apple Banana"
print(c)

d = """
    Apple
    'Banana'
    "Coconut"
    Durian
"""
print(d) # """, '''안에는 enter와 '' , ""등등을 넣을 수 있음

print(type(d)) # <class 'str'>

# 혼합
e = 'apple"banana"coconut\'durian\''
print(e)
f = "apple 'banana' coconut \"durian\""
print(f)  # '를 쓰면 안에 "를 쓰고 "를 쓰면 안에 '를 쓴다.

# 문자열 연산 (더하기, 곱하기
str01, str02 = 'Hello, ', 'World'
print(str01 + str02)
print(str01 * 2 + str02) # 곱하기는 해당 문자열을 반복 출력

