# dictionary
# dict : 딕셔너리(사전)
# 자바의 Map 처럼 값을 key와 value로 묶어 하나씩 저장하는 자료형

# 생성자 사용
dict01 = dict()
dict01[1] = 100
dict01[2] = 200
print(dict01)

# {}로 만들기
dict02 = {}
dict02['one'] = 1
dict02['two'] = '두번째입니다'
dict02['three'] = '삼삼이'
print(dict02) # dict02[]. [] 안에는 key값

# key/value 가져오기
print(dict01.get(1))
print(dict02['one']) # get과 대괄호 방식은 찾는 방식은 동일하나 없는 key를 찾을 때
                     # 대괄호는 에러가 나고 get은 none을 찾아줌
                     # get이 더 안정적임.

print(dict01.keys()) # dict_keys([1, 2]) 결과가 list처럼 되어있음
print(dict01.values())

print(list(dict02.keys())[1]) # 결과값이 list처럼 되어 있으니까 list로 접근하기

