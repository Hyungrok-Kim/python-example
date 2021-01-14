'''
별짓기
*
**
***
****
*****
'''
#실습 1
# 문자열 * n : 문자열을 n번 반복한다.
for i in range(5): # 0~4까지를 의미함
    print('*' * (i + 1))
print('-----------')

# java로 하면
# public class Main{
#   public static void main(String[] args){
#       for(int=1; i < 6; i++){
#            for(int j=1; j < i; j++){
#                   System.out.println('*');
#            }
#            System.out.println();
#       }
#   }
# }

# 실습 2
'''
*****
****
***
**
*
'''
# Plan A
for i in range(5,0,-1):
    print('*' * (i))
print('-----------')

# Plan B
for i in range(5):
    print('*' * (5-i))
print('-----------')

# Plan C
print('\n'.join([''.join(['*' for i in range(i)]) for i in range(5,0,-1)]))
print('-----------')


# 실습 3
'''
    *     --> ' ' * 4, '*' * 1
   **     --> ' ' * 3, '*' * 2
  ***     -->        ...
 ****
*****     --> ' ' * 0, '*' * 5
'''
print('=====')
for i in range(1,6):
    print(' ' * (5-i) + '*' * (i))

print('-----')

# 실습 3
'''
    ☆
   ***
  *****
 *******
*********
   ***
'''
# Plan A
start = 1
end = 6
for i in range(start,end):
    if(i == start):
        print(' ' *  (5-i) + '☆' + ' ' * (5-i))
        continue
    print(' ' * (5-i) + '*'*(i-1) + '*' + '*'*(i-1) + ' ' * (5-i))

    if(i == (end-1)):
        print(' ' * 3 + ('*' * 1) + '*' + ('*' * 1) + ' ' * 3)
print('========')

# Plan B
for i in range(6):
    gap = 4 - i
    if i == 0:
        print(' ' * gap + '☆')
    elif i < 5:
        print(' ' * gap + '*' * (2 * i + 1))
    else:
        print(' ' * 3 + '***')
print('---------')

# Plan C
for i in range(6):
    if i == 0:
        print('{:^9}'.format('☆'))
    elif i < 5:
        print('{:^9}'.format('*' * (2 * i + 1)))
    else:
        print('{:^9}'.format('***'))


# 피보나치 알고리즘 구현하기
n = input('반복할 횟수 : ')
a, b = 0,1
i = 0
while i < int(n):
    print(a, end=' ')
    a, b = b, a+b
    i += 1
print()
