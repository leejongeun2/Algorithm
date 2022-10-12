# 어떤 배추에 지렁이가 한마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동 가능하여 보호 받을 수 있음
# 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우 서로 인접한 것임
# 필요한 지렁이 마리수 출력
from collections import deque

dx = [0,0,1,-1] # 아래, 위, 오른, 왼
dy = [1,-1,0,0]

t = int(input())

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b)) # 배추자리 추가
    graph[a][b] = 0 # 배추자리 0으로 바꾸기

    while queue: 
        x, y = queue.popleft() # 배추자리 빼기
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m: # 음수가 되면 표를 벗어나기 때문, 그리고 각 표의 길이를 초과하면 안되기 때문
                continue
            if graph[nx][ny] == 1: # 사방에 1이 있다면
                graph[nx][ny] = 0 # 배추있는 자리를 0으로 바꿔줌
                queue.append((nx, ny)) # 배추있는 것을 다시 탐색
    return

for i in range(t):
    cnt = 0
    n, m, k = map(int,input().split()) # 10, 8, 17
    graph = [[0]*m for _ in range(n)] # 가로길이 겉 리스트, 세로 길이 속 리스트 생성 

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1 # 배추 표시

    for a in range(n):
        for b in range(m): # 각 배추 자리 모두 탐색
            if graph[a][b] == 1: # 배추 있다면 함수 실행하여 사방 탐색
                bfs(graph, a, b)
                cnt += 1 # 기준배추 사방 탐색 후 사방에 배추가 있을 때 그 배추 사방 탐색하고, 0으로 만들어줌 => 각 배추마다 사방탐색하고 cnt +=1
    print(cnt)