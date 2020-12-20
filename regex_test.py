import re

'''
Regular Expression
. : 문자 1개
^ : 문자열의 시작
$ : 문자열의 마지막
[] : 문자의 집합
| : OR
() : 괄호 안의 정규식 그룹

* : o or more
+ : 1 or more
? : 0 or 1
{n} : n번 반복
{n,m} : n번 부터 m번
{n,} : n번 부터 무한번
'''

"""
r 문자열 표기법 (re 모듈의 확장 문법)
\w : [a-zA-Z0-9_] : a~Z, 0~9, _ 포함하는 모든 문자
\W : [^a-zA-Z0-9_] : 위의 문자 제외한 나머지 문자
\d : [0-9] : 0 부터 9
\D : [^0-9] : 숫자 제외한 나머지 문자
\s : [\t\n\r\f\v] : 공백문자
\S : [^\t\n\r\f\v] : 공백 제외한 모든 문자
\b : 단어의 시작과 끝의 빈 공백
\B : 단어의 시작과 끝이 아닌 빈 공백
\\ : \
\[숫자] : 지정된 숫자만큼 일치하는 문자열
\A : 문자열의 시작
\Z : 문자열의 끝
"""

# match('패턴', 문자열) : 문자열 시작부터 비교
'''
str01 = input('영단어를 입력하세요 : ')
print('영단어 입력 확인 : ', re.match('[a-zA-Z]', str01))
'''

# search('패턴', 문자열) : 일치하는 문자열 확인(시작부터 비교 x)
'''
str01 = input('영단어 여러 개를 ,로 구분지어 입력하세요 : ')
result = re.search('[a-zA-Z]+', str01) # +는 반복
print(result)
'''

# findall('패턴', 문자열) : 특정 문자열과 일치하는 값들을 리스트 형태로 반환하는 함수
'''
str01 = input('영단어 여러개 입력 : ')
result = re.findall('[a-zA-Z]+', str01)
print(result)
'''

# Match 객체의 함수들
# groups() : 패턴에 맞는 문자들
# group(순번) : 해당 순번의 찾은 문자
# start() : 검색이 시작된 문자 순번
# end() : 마지막 검색한 문자 순번

result = re.match('(\d{4})-(\d{2})-(\d{2})', '2020-12-09')
print(result.groups())
print(result.start())
print(result.end())
print(result.group(0))   # 0번째 그룹은 다 나옴. 1번째는 2020, 2번째는 12, 3번째는 09

# 실습 1
# 여러 이메일을 입력받아 해당 이메일의 아이디들을
# 추출하여 리스트로 출력해보세요.
# [이메일 형식] : 0000@example.com --> id는 0000

em = input('이메일 여러 개 입력 : ')
res = re.findall('(\w{1,})@(\w{1,}).(\w{1,})', em)   # 모든 문자열 1이상 반복, 괄호를 쳐주면 탐색조건이 돼서 @ 떼고 찾아줌
print(res)

