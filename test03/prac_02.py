# 랜덤 숫자 random

import random

rn1 = random.random()
print(rn1)

# random의 불편함 때문에 생긴게 randint
# randint(시작값, 끝값)
rn2 = random.randint(1, 45)  # 1~45까지 찍어줌 자바와 다르게. 자바는 1,46이라고 해야 45까지 찍어줌
print(rn2)

# 총 실습 1
# 1 ~ 10까지 중 임의의(랜덤한) 수를 고른 후
# 숫자를 하나 입력 받아
# 맞췄으면 '정답입니다.'
# 만약 선택한 숫자보다 랜덤한 숫자가 높으면 'UP!'
# 만약 선택한 숫자보다 랜덤한 숫자가 낮으면 'DOWN!'
# 이라고 출력하는 코드 작성해보기 ( 일단 반복 X )
'''
rannum = random.randint(1,10)
myans = int(input('정수(1~10)하나 입력 : '))
if myans is rannum:
    print('정답입니다.')
elif myans > rannum :
    print('UP!')
else :
    print('DOWN!')
'''

# 반복 있는 버전
# 실습 2 : UP & Down (with 반복문)
# 위의 코드를 응용하여
# 사용자가 정답을 맞출 때까지 반복하여
# UP & Down을 실행하는 코드를 작성하시오
'''
rannum = random.randint(1,10)
while True:
    myans = int(input('정수(1~10)하나 입력 : '))
    if myans is rannum:
        print('정답입니다.')
        break
    elif myans > rannum:
        print('UP!')
    else:
        print('DOWN!')
'''
# 총 실습 3
# computer = random.randint(0,2) 와
# rps = {0:'가위', 1:'바위', 2:'보'} 사전 자료형을 활용하여
# 가위바위보 게임을 만들어 보세요
# 예시)
# 입력 : 가위
# 컴퓨터 : 바위
# 컴퓨터가 이겼습니다!
# ---------------------------
# 입력 : 보
# 컴퓨터 : 바위
# 당신이 이겼습니다!
# ---------------------------
# 입력 : 바위
# 컴퓨터 : 바위
# 비겼습니다!

# Plan A
computer = random.randint(0,2)
computerans = ''
rps = {0:'가위' , 1:'바위', 2:'보'}
rps.items()
if computer == 0 :
    computerans = '가위'
elif computer == 1 :
    computerans = '바위'
elif computer == 2 :
    computerans = '보'
else :
    print('잘못입력')

myrps = input('가위바위보 입력 : ')
print('컴퓨터 : ' ,computerans)
if myrps == '가위':
    myrpsnum = 0
elif myrps == '바위':
    myrpsnum = 1
elif myrps == '보' :
    myrpsnum = 2
else :
    print('잘못입력했어')

if myrpsnum == computer:
    print('비겼습니다.')
elif computer == 0 and myrpsnum == 1:
    print('이겼습니다.')
elif computer == 1 and myrpsnum == 2:
    print('이겼습니다.')
elif computer == 2 and myrpsnum == 0:
    print('이겼습니다.')
else:
    print('졌습니다.')

#Plan B (딕셔너리, items, get 사용)
computer2 = random.randint(0,2)
rps2 = {0:'가위' , 1:'바위', 2:'보'}
answer3 = input('입력 :')

for k, v in rps.items():
    if answer3 != v:
        continue
    else:
        print('컴퓨터 : ' + rps.get(computer2))
        if computer2 == k :
            print('비겼습니다!')
        elif computer == k + 1 or k - 2 == computer :
            print('컴퓨터가 이겼습니다.')
        else :
            print('당신이 이겼습니다.')





