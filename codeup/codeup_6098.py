# 미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
# 먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.


array = []

for i in range(10): 
    array.append(list(map(int, input().split())))

x, y = 1, 1 # 2,2 개미집이라서 여기서 출발(인덱스 기준)

while True:
    if (array[x][y] == 0): # 갈 수 있는 곳이라면
        array[x][y] = 9 # 9로 표시
    elif (array[x][y] == 2): # 먹이가 있다면
        array[x][y] = 9 # 9로 표시하고 
        break # 멈춤

    if ((array[x][y+1] == 1 and array[x+1][y] == 1)): # 옆으로 가거나, 아래로 갔을 때 막혔다면 멈춤
        break

    if (array[x][y+1] != 1): # 옆으로 갔을 때 1이 아니라면
        y = y + 1 # (1,2)
    elif (array[x+1][y] != 1): # 밑으로 갔을 때 1이 아니라면 
        x = x + 1 # (2,1)

for i in range(10):
    for j in range(10):
        print(array[i][j], end=' ')
    print()
# if의 나열은 이전 if 충족 여부 상관없이 계속 if가 효력이 있는거고, elif는 앞의 if가 충족하지 않을때만 효력이 있다