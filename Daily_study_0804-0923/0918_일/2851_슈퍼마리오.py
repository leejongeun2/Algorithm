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
# 예를 들어 result값이 100이 었을 때, 0 <= 100-(100-40) => 40
# 즉, 바로 전 것(전 값까지의 합)과의 차이를 비교해서 현재 차가 더 적다면 멈춤 
            break
        else:
            result -= i # 아닌 경우, 전 것을 출력
            break
print(result)
