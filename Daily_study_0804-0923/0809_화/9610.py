# 사분면

n = int(input())

q1 = 0 # 변수 셋팅을 for문 밖에 해야함
q2 = 0
q3 = 0
q4 = 0
axis = 0

for _ in range(n):
    a, b = map(int, input().split())
    if a == 0 or b == 0:
        axis += 1
    elif a > 0 and b > 0:
        q1 += 1
    elif a < 0 and b > 0:
        q2 += 1
    elif a < 0 and b < 0:
        q3 += 1
    elif a > 0 and b < 0 :
        q4 += 1


print(f'q1: {q1}') # f스프링 활용법



 

