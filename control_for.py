# for 반복문
# python은 for-in 문이라고 한다. for랑 in이 세트가 되어야 함

subject = ['java', 'sql', 'python']
for i in subject:
    print(i, end=' ') # 끝날 때 띄워쓰기로 구분해주세요. end=' '
else :
    print(' 참 재밌다!')

# range(시작값, 끝값-1, step) : 시작 값부터 끝값 전까지 step 만큼
#                             숫자를 반복하는 함수

for i in range(1, 100):
    print(i, end=" ")
else :
    print(' 끝 ')

# 실습 1
# 2 ~ 9까지 숫자를 하나씩 반복해 출력하는
# 반복문을 작성하세요
for i in range(2,10):
    print(i, end=" ")

print()
# 실습 2
# 1 ~ 9까지 숫자를 하나씩 반복해
# 출력하는 반복문을 작성하세요
for i in range(1,10):
    print(i, end=" ")
print()
# 자바였다면
# for(int i = 1; i < 10; i++){
#   System.out.println(i)
# }

# 실습 3
# 변수 i와 j를 사용하여
# 위의 두 반복문을 중첩사용(겹쳐서 사용)하여
# 구구단을 만들어 보세요.
# 출력 예시
# << 2 단 >>
# 2 * 1 = 2
# 2 * 2 = 4
#   . . .
# << 3 단 >>
# . . . .
for i in range(2,10):
    print('<< {} 단 >>'.format(i))
    for j in range(1,10):
        print('{} * {} = {}'.format(i , j , i * j))

# reverse 버전
for i in range(10, 0, -1):
    print(i, end='\t')

