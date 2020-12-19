# operation

# 산술 연산자
# 사칙 연산 ( +, -, *, /, %, //)
a = 20
b = 3
print(a + b) ### 덧셈
print(a - b) ### 뺄셈
print(a * b) ### 곱셈
print(a / b) ### 나눗셈 ( 정수 나눗셈은 결과가 실수다. )
print(a % b) ### 나머지 연산(modular 연산)

## Alt + Shift + F10 (강제 실행) (PyCharm)
## Shift + F10 (직전 코드 재실행)

# 제곱 연산 20의 세제곱
print(a ** b) ### a에 대한 b만큼의 제곱 수 연산 a^3

# 몫 연산 : 소숫점 이하 버리기 (floor division) (내림 나누기)
print(a // b)

# 비교 연산자와 논리 연산자
a, b = 5, 3
print(a == b) ## False
print(a != b) ## True
print(a > b)  ## a가 b보다 큰가? --> True
print(a <= b) ## a가 b보다 작거나 같다 --> False
print(a is b) ## 값 자체 뿐만이 아닌 객체 비교 연산자 ( a가 b랑 같은 애냐? ) --> False
print(a is not b) ## a가 b랑 같은 애가 아니냐? --> True
## is 는 java의 .equals()와 같음
## ==는 값 자체를 비교하는 거고 is는 실제 저장된 메모리의 주소까지 비교하는 것
## is는 같은 객체인지 비교
a = [1,2,3]
b = a
c = [1,2,3]
print(id(a))
print(id(b))    # a와 b는 같은 메모리 주소를 사용해서 완전히 같음.
print(id(c))    # c와는 메모리 주소가 다름. 값 자체는 같지만
print(a is b)
print(c is b)

# 논리 연산자
print(True or False)            ## Java로 치면 (||) : ~이거나
print(True | False)

print( (10 > 5) or (10 >= 15) ) ## 앞쪽은 True나오고 뒷 쪽은 False 나오고, or이라서 True가 나온다.

print(False and True)           ## Java로 치면 (&&) : ~ 이면서
print((10 > 5) and (10 <= 100)) ## 앞쪽 뒷쪽 다 True이기 때문에 True
print((10 > 5) & (10 <= 100))

print(not False)                ## Java로 치면 ! : 논리 결과의 반대
print(not (10 > 20))            ## not False --> True

# 범위 연산자
list01 = list(range(100))  # 0 ~ 99
print(list01)

# [시작 순번 : 끝 순번] --> 시작 ~ 끝 - 1
# [시작 : 끝 : 스탭] --> 시작 ~ 끝 - 1, 스탭 만큼 건너 뜀

print(list01[2])           # 2
print(list01[10:20])       # 10 ~ (20 - 1)
print(list01[10:20:2])     # 10 ~ 19, 2씩 건너뜀 (step)

str01 = 'Hello World!'
print(str01)
print(str01[0])            # 'H'
print(str01[0:5])          # 'Hello' 0부터 시작해서 5전까지 0~4
print(str01[0:5:2])        # Hlo
print(str01[0:4]*2)        # HellHell

# reverse (거꾸로 뽑기)
print(str01[-2])           # 끝에서부터 2번째
print(str01[-2:])          # 끝에서부터 2번째 위치를 찾고 그 위치부터 마지막까지, 즉 d!
print(str01[:-2])          # 처음부터 -2의 위치 전까지 뽑겠다.
print(str01[::-2])         # !lo le 뒤에서부터 앞으로 2칸씩 찾음

# 멤버 연산자(in / not in)
list02 = ['귤', '딸기' , '뀰', '망고', '홍시', '슐', '뮬', ]
str02 = input('과일을 선택하세요 : ')
print(str02)
print(str02 in list02)
print(str02 not in list02)

# 실습 1
# 문자열 '안녕하세요, 반갑습니다!' 에서
# '반갑습니다' 만 추출해보기
str03 = '안녕하세요, 반갑습니다!'
print(str03[7:-1])

# 실습 2
# 문자열 'Python'을 활용하여
# 'PyPyon' 단어를 만들어 보세요.
str04 = 'Python'
print(str04[:2] +'Py' + str04[4:])
print(str04[:2] * 2 + str04[4:])

# 실습 3
# list03 = [1, 2, 3, 4, 5, 9 ,0, 15]
# 리스트를 생성하여 오름차순 정렬 후
# 범위 연산자를 활용하여 결과를 역순으로 뽑아 보세요
list03 = [1,2,3,4,5,9,0,15]
list03.sort()
print(list03[::-1])



















