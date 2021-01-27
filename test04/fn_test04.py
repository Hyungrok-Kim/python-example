# 일반 함수식과 람다 비교하기

def mySum(x, y):     # ()안에 *args를 쓰면 매개변수로 들어오는 것 다 더하겠다. 라는 의미
    return x + y
if __name__ == '__main__':
    a = mySum(10,20)
    print(a)

    print((lambda x, y : x + y)(10,20))