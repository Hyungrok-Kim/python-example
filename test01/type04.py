# list

# 생성자를 통한 객체 생성
a = list()
print(a)
a.append(1)
print(a)
a[0] = 'a'
print(a)
# list 안에 존재하지 않는 순번의 값은 접근이 불가능하다.
# 값을 '추가'할 때는 반드시 append() 함수를 사용해야 한다.
# a[1] = 10  # list assignment index out of range
# print(a)

# [] 사용
b = [1,2,3,4,5]
print(b)

# 값 사용하기 - 파이썬도 시작은 0부터이다. zero based index
print(b[0] + b[2])

# 값의 순서를 역순(reverse)으로 뒤집기
b.reverse()
print(b)

# 정렬하기
b.sort()
print(b)

# 리스트 중첩 사용
c = ['a', 'b' , 'c', 'd', ['e', 'f', 'g'], 'h']
print(c)
print(c[4])
# 안에 들어있는 f값이 뽑고 싶을 때
print(c[4][1])

# list + list : 리스트 합치기
print(b + c) # [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', ['e', 'f', 'g'], 'h']







