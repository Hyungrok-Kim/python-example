# 람다식
# define인 def를 만들기 귀찮거나 사용하지 못하는 경우에 lambda를 사용
# 람다는 익명 함수의 역할을 함

hap01 = lambda x,y : x + y
print(hap01(10, 5))

a = [(1, 'one', 9), (2, 'two', 8), (3, 'three', 7), (4, 'four', 6)]
b = []
for i in a:
    for j in a:
        if i[1] < j[1]:
            b.append(i)
        else :
            b.append(j)

a.sort(key= lambda x:x[1])
print(a)
print(lambda a:a[1])

# 람다 전용 if 표현식 : 값1 if 조건식 else 값2 ## 조건식이 성립한다면 값1을 뽑고 그게 아니라면 값2를 뽑아라
min01 = (lambda x, y : x if x < y else y)(50,20) # 람다 문법이 따로 있음.
print(min01)

max01 = (lambda x, y : x if x > y else y)(10, 20)
print(max01)

def max02(x,y):
    if x > y:
        print(x)
    else:
        print(y)

print(max02(10,20))
