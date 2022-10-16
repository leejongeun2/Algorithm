# 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림중 넓이가 가장 넓은 것의 넓이를 출력
# 그림이라는 것은 1로 연결 된 것을 한 그림, 가로나 세로로 연결 된 것은 연결, 대각선은 연결아님
# 그림의 넓이란 그림에 포함 된 1의 개수
# 유기농 배추 문제와 같이 사방탐색
import sys
from collections import deque
input = sys.stdin.readline
 # 어떤게? bfs => 최단거리
def bfs(x, y):
    each_cnt = 1    # init each_cnt
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
 
    while queue:
        x, y = queue.popleft()
 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    each_cnt += 1    # 1이 있을 때, 덱에 넣었을 때
    return each_cnt    # end each_cnt
 
n, m = map(int, input().split()) # 도화지의 세로 크기, 가로크기
visited = [[False] * m for _ in range(n)] # 예제에서 주어진 크기만큼 false로 이루어진 2차원 배열만듬
graph = [list(map(int, input().split())) for _ in range(n)] # 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분
# 문제와 똑같은 값으로 이루어진 이차원 배열 만듬


dx = [1, 0, -1, 0] # 아래, 오른, 위, 왼
dy = [0, 1, 0, -1]
 
cnt, max_each_count = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]: # (0,0)이 1이고 false라면
            cnt += 1    # dfs work condition, 그림 시작
            max_each_count = max(max_each_count, bfs(i, j)) # bfs에 i,j넣어서 리턴한 값, 그리고 그 값과 계속 넣어진 값을 비교할 것임
 
print(cnt) # 그림의 개수
print(max_each_count) # 그 중 가장 넓은 그림의 넓이