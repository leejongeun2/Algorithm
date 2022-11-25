# 여행가 a는 n*n크기의 정사각형 공간 위에 서있다. 
# 가장 왼쪽, 위 좌표는 (1,1)이며 가장 오른쪽 아래 좌표는 (n,n)이다. 
# 여행가는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작좌표는 항상 (1,1)이다. 
# 상하좌우 어디로 이동할건지 주어짐
# 일련의 명령에 따라서 개체를 차례대로 이동시킨다는 점에서 시뮬레이션 유형으로 분류

n = int(input()) # 주어진 정사각형
x, y = 1, 1 # 출발 시점
plans = input().split()

dx = [0, 0, -1, 1] # 왼, 오, 위, 아래
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for plan in plans: # 이동 계획(알파벳)을 하나씩 확인
    for i in range(len(move)): # 이동 후 좌표 구하기
        if plan == move[i]: # 왼쪽일 때(L일때)
            nx = x + dx[i] 
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n: 
        continue # 공간을 벗어나는 경우 무시
    x, y = nx, ny # 이동 수행
print(x, y)

