# if else 구문
# 파이썬에서는 if elif else

# if else 1
i = 1;
if i==1:
    print('i == 1')
    # 들여쓰기는 공백 문자 2개 또는 4개 또는 tab 기호를 권장한다.
    # 파이썬은 들여쓰기로 구분을 짓는다.
else :
    print('i != 1')

# 자바에서는
# int i = 1;
# if(i == 1){
# System.out.println("i==1");
# }
# else{
# System.out.println("i!=1");
# }

# if elif else
i = 1
if i == 1 :
    print('i == 1')
elif i == 2 :
    print('i == 2')
else :
    print('i != 1 and i != 2')

# 실습 1
# 사용자에게 정수를 입력받아
# 짝수인지, 홀수인지 출력하는 코드를 작성하세요.
num = int(input('정수 입력 :'))
if num % 2 == 0 :
    print('짝수입니다.')
else :
    print('홀수입니다.')

# 실습 2
# fruitsBox = ['귤', '슐', '뀰', '뮬', '츌']
# 리스트를 하나 생성하고, 문자를 입력받아
# 과일박스(fruitsBox)에 존재하는 상품인지 확인하여
# 존재하면 '있는 과일입니다!'
# 존재하지 않으면 '없는 과일이네요~!'를
# 출력하는 코드를 작성하세요
fruitsBox = ['귤', '슐', '뀰', '뮬', '츌']
str = input('과일 입력 :')
if str in fruitsBox :
    print('있는 과일입니다.!')
else :
    print('없는 과일이네요~')


# 실습 3
# 다음 점수표를 보고
# 사용자에게 score를 입력받아 학점을 출력하는 코드를 작성하세요
# ---------------
# 학점 | 점수(score)
# ---------------
#   A  | 90 ~ 100
#   B  |  70 ~ 89
#   C  |  50 ~ 69
#   D  |  30 ~ 49
#   F  |   0 ~ 29
# ----------------

score = int(input('점수 입력 :'))
if score >= 90 :
    print('A')
elif score >= 70 :
    print('B')
elif score >= 50 :
    print('C')
elif score >= 30 :
    print('D')
else :
    print('F')

