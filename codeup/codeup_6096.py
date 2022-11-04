# 그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후, 
# 다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것이다.
# 어떤 위치를 골라 집자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀐다.

location = []

for i in range(19): # 이중 리스트 생성
    location.append([])

    for j in range(19):
        location[i].append(0)

for i in range(19): # 한 줄 
    location[i] = list(map(int, input().split())) # 각 리스트 안의 리스트에 값 넣기

n = int(input()) # 십자 뒤집기 횟수

for i in range(n): 
    x, y = map(int, input().split()) # 입력 받은 것은 1부터 시작 기준(인덱스 기준 아님)

    for j in range(19):
        if location[x-1][j] == 0:  # 인덱스 기준이 아니어서 1을 빼는 것임
            location[x-1][j] = 1
        else:
            location[x-1][j] = 0
        if location[j][y-1] == 0:
            location[j][y-1] = 1
        else:
            location[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(location[i][j], end=" ")
    print()