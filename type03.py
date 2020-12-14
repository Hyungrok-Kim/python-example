# type01, type02의 자료형을 활용한 간단한 입출력 구현하기

# 출력
a = 10
b = 'A'
print(a)
print(b)
# 서로 다른 자료형은 + 로 합칠 수 없다!
# print(a + b)
# 만약 여러 자료형을 연이어 출력하려면 ',' 형식으로 나열하면 된다.
print(a, b)

# +a (sep, end 옵션)
# sep : 구분자 직접 선언하는 방법
# end : 출력의 마지막에 붙일 내용 (end를 명시할 경우, 끝에 \n을 직접 지정해야 한다)
num1, num2, num3 = 10, 20, 30
print(num1, num2, num3, sep='@', end='! \n')

# input() : 입력 함수
str01 = input('문자열을 하나 기록하세요 : ')
print('입력한 문자열 : ' , str01)

# 실습 1
# 학생의 학년, 반, 번호, 이름을 입력받아
# "n학년 n반 n번 학생은 000 입니다." 문자열 출력하기
grade = input("학년 :")
sclass = input("반 :")
snum = input("번호 :")
sname = input("이름 :")
print(grade,'학년' ,sclass,'반' ,snum,'번 학생은', sname,'입니다.')

# 위의 내용이 불편하기 때문에
# format 함수 사용하기
print('{0} 학년 {1} 반 {2} 번 학생 이름은 {3} 입니다.'.format(grade,sclass,snum,sname))

# 실습 2
# 학생 이름과 국어, 영어, 수학 점수를
# 각각 name, kor, eng, mat 변수에 입력받고
# 해당 학생의 총점과 평균을 아래와 같이 출력하는
# 코드를 작성하세요.
# [출려 결과]
# '000 학생의 평균은 70.0점, 총점은 210점 입니다.'

name = input('이름 :')
kor = int(input('국어 :'))
eng = int(input('영어 :'))
mat = int(input('수학 :')) # input으로 받으면 무조건 str로 인식하기 때문에 int로 바꿔줌
total = kor + eng + mat
avg = total/3

print('{}학생의 평균은 {:.1f}점, 총점은 {}점 입니다' .format(name, avg, total))
#                   소숫점 첫째자리까지만 해달라!
#                   사실 이렇게 안해도 소숫점 첫째짜리까지만 나오긴 함




