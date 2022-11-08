# 지역의 높이 정보를 파악, -> 그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇개가 만들어지는지? 
# 비의 양에 따라서, 물에 잠기지 않는 안전한 영역의 개수는 다르기 때문에 비의 양에 따른 모든 경우를 조사해보면 물에 잠기지 않는 안전한 영역의 개수중에서 최대인 경우가 있음
# 어떤 지역의 높이의 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수 출력
import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = []
max_num = 0
result = 1

dx = [0,0,-1,1] # 오, 왼, 위, 아래
dy = [1,-1,0,0]

for i in range(n):
    low = list(map(int, input().split()))
    graph.append(low) # row 하나씩 그래프에 넣어서 이중 리스트 만듬(단, 밑에for문으로 각 리스트 확인하고 low리스트 추가)

    for j in low:
        if j > max_num: # 0보다 크면 max_num row값으로 갱신, 각 줄에서 제일 큰 값을 max_num(2차원 배열 중 가장 큰 값)
            max_num = j

def dfs(x,y,num): # def만나면 밑에 for문으로 가기(def는 함수를 정의한것이니까)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0: # 표 안에서 움직여야하고, 방문하지 않았으면(dfs는 다시 돌아오므로, 오는길인 경우) 
            if graph[nx][ny] > num: # num은 33번째줄의 i임(0) 즉, 건물 높이가 비의 양보다 작은 경우(0인 경우) 방문할 수 없음
                visited[nx][ny] = 1 # 방문 처리
                dfs(nx,ny,num) # 5*5 배열이 i(0)에서 모두 방문 처리 된다면 이전 dfs값으로 돌아감

for i in range(1, max_num+1): # 2차원 배열에 가장 큰 값만큼 반복 => 각 지역의 높이 개수 경우의 수를 탐색해줌!
    visited = [[0]*n for _ in range(n)] # 5*5 0으로 이루어진 배열
    cnt = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0: # 첫번째 i=0일때, 0보다 크거나, 0이랑 같을 때
                cnt += 1 # 숫자 증가
                visited[j][k] = 1 # 방문체크
                dfs(j,k,i) # 첫번째: (0, 0, 0)
    result = max(result, cnt)

print(result)