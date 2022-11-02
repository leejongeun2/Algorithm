# 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
# n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.

d = [] # 0이 20개 있는 리스트가 20개있음
for i in range(20):
    d.append([]) # 리스트 안의 리스트에 아래 0 추가, 리스트 안의 리스트가 d[i]임
    for j in range(20):
        d[i].append(0) # 리스트 안에 들어있는 리스트안에 0 추가해 넣기

n = int(input()) # 바둑판에 올려놓을 흰 돌의 개수(n)이 출력
for i in range(n):
    x, y = input().split() # 흰돌을 놓을 좌표(n은 10이하의 자연수이고 x, y 좌표는 1 ~ 19 까지)
    d[int(x)][int(y)] = 1
    
for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print() # 한줄씩 줄바꿈




