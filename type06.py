# set(집합) : 중복 x, 순서 x

# 생성자 사용
a = set(['1', '2', '3', '4', '4'])
print(a) # 중복이 허용되지 않기 때문에 두 번 들어간 '4'는 한번만 나옴
         # 순서도 자기 마음대로 나옴
# set은 {}

# 문자열을 넣으면 문자 하나하나로 쪼개는 역할도 함.
b = set('hello')
print(b)  # {'h', 'l', 'e', 'o'}

# [] = list
# () = tuple
# {} = set
c = { 'a' , 'b' , 'c', 'hello', '1' , '2', '3'}
print(c)

# set 값 추가
c.add('word')
print(c)

# 합, 교, 차집합
# 합집합 : 두 집합을 하나로 합치는 방법( | ) 또는 union
a = {1, 3, 4}
b = {2, 4, 8}
print(a | b)
print(a.union(b))

# 교집합 : 두 집합에서 겹치는 부분을 추출하는 방법( & ) 또는 intersection
print(a & b)
print(a.intersection(b))

# 차집합 : 원본 집합에서 다른 집합과의 공통 요소를 뺀 나머지 ( - ) 또는 difference
print(a - b)
print(a.difference(b))

