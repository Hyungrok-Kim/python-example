# 내가 만든 .py 파일을 모듈로 추가하여 사용하기
# File > settings > Project -> Project Structure
# 에서 모듈로 사용하고자하는 패키지 또는 파일을 마우스 우클릭으로 source로 지정해야함.

# File > settings > Project -> Project Interpreter에서
# + 버튼을 클릭해 numpy와 matplotlib (모듈)라이브러리를 install해준다.

# import fn_test05
from fn_test05 import fibo1

n = int(input('숫자 입력 :'))
fibo1(n)




