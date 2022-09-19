# 10개의 버섯이 일렬로 놓여졌있다. 
# 100애 가장 가까운 수 

m = []

for k in range(10):
    m.append(int(input()))

result = 0
for i in m:
    result += i # result 변수에 입력 값을 더해주기
    if result >= 100: # 더해준 것들이 100이 넘는다는 것들 안에서
        if abs(result-100) <= abs(100-(result-i)): 
# 딱 result값이 100이 었을 때, 0 <= 100-(100-40) => 40
            break
        else:
            result -= i # 아닌 경우, 다음 것을 뺀다,
            break
print(result)
