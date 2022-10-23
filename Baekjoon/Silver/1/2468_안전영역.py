import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = []
max_num = 0
result = 1

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(n):
    low = list(map(int, input().split()))
    graph.append(low) # row 하나씩 그래프에 넣어서 이중 리스트 만듬(단, 밑에for문으로 각 리스트 확인하고 low리스트 추가)

    for j in low:
        if j > max_num: # 0보다 크면 max_num row값으로 갱신, 각 줄에서 제일 큰 값을 max_num(2차원 배열 중 가장 큰 값)
            max_num = j

def dfs(x,y,num):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0: # 표 안에서 움직여야하니깐
            if graph[nx][ny] > num:
                visited[nx][ny] = 1
                dfs(nx,ny,num)

for i in range(max_num): # 2차원 배열에 가장 큰 값만큼 반복
    visited = [[0]*n for _ in range(n)] # 5*5 0으로 이루어진 배열
    cnt = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                cnt += 1
                visited[j][k] = 1
                dfs(j,k,i)
    result = max(result, cnt)

print(result)