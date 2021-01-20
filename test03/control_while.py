# 파이썬은
# i++, i--가 없다. i+=1, i-=1으로 구현해야함.

# while 반복문

i = 1
while i <= 10:
    print(i)
    i += 1 ## python은 i++, i-- 없다.
else:
    print('~~끝났다 ~~')

# 실습1
# while 반복문과 mySum, i 변수를 사용하여
# 1 ~ 10까지의 합을 구하고
# else에서 그 결과 mySum을 출력하는 코드를 작성하세요.
i = 1
mySum = 0
while i <= 10:
    mySum += i
    i += 1

else :
    print('1에서 10까지의 합 : ', mySum)


