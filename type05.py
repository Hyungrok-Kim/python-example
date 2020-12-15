# tuple : list와 거의 동일하나 값 변동 x

# 생성자를 사용
# 리스트는 [] 였다면 tuple은 ()
a = tuple()
print(a)
b = tuple([1,2,'3'])
print(b)

# () 사용
c = (1,2,3,4)
print(c)

# 값 변경(추가, 삭제, 변경) 불가
# a.append(10) -- tuple에는 append 없음
# b[1] = 100 -- 'tuple' object does not support item assignment
# item 할당할 수 없음 , 값 직접 변경 X

# 튜플을 사용하는 이유
# 어떠한 경우에도 변경이 되어서는 안되는 불변적인 정보 ex)지난 달의 기상정보,
# 일주일과 같은 일정한 단위 , 예년도 통계 수치

# tuple + tuple
# 튜플끼리는 서로 내용을 더할 수 있음.
d= tuple(range(3, 6)) # 3부터 6전까지
print(d)
print(b + d)

# tuple -> list로 바꾸기
e = list(d)   # 튜플인 d를 list로 바꾼다.
e.append('6')
print(e)
# list -> tuple
f = tuple(e)
print(f)

# unpacking
# 안의 값들을 변수의 갯수에 맞춰 하나씩 풀어 헤칠 수 있음
num1, num2, num3, num4 = f
print(num1 , num2 , num3 , num4)






