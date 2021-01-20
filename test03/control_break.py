# break / continue

# 어떠한 문장을 실행했을 때 뛰쳐나가는게 break
i = 1
while i <= 10:
    if i > 5:
        break
    print(i)
    i += 1
else :
    print('i = ' , i) # 출력이 안된다.

# while에서 else까지가 한 몸이기 때문에 break문으로 나가게 되면 else문에 있는 것도
# 실행하지 않음.

print('-----------------')

# continue
# 나 재끼고 이어서 해주세요.
# continue에 해당이 되면 아랫줄로 넘어가지 않고 다시 반복을 하는 for 쪽으로 이동함
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)
else :
    print("i = ", i)  # 출력이 된다.






