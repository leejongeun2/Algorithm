# 1번 컴퓨터가 바이러스 걸렸을 때, 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램 작성
# => 1번 컴퓨터랑 연결 된 컴퓨터

n = int(input()) # 컴퓨터의 개수
link = int(input()) # 연결선 개수

network = []

for _ in range(n+1):
    network.append([]) #인덱스 기준이니 1~7번이 들어갈 8자리 빈 리스트 생성
print(network)

# print(network)
for i in range(link):
    a, b = map(int, input().split())
    network[a].append(b) # 1의자리에 2를 넣어줌 (a에 b연결) => 쌍방 연결 되있음을 표시
    network[b].append(a) # 2의자리에 1을 넣어줌 (b에 a연결) => 쌍방 연결 되있음을 표시

visited = [0]*(n+1) # 해당 컴퓨터를 방문했는지 체크해주는 곳

def dfs(v): # 방문할 컴퓨터 번호 
    visited[v]=1 # 방문표시
    for j in network[v]: # network[1]은 1번컴퓨터에 연결된 컴퓨터들의 리스트 들을 순회 => 그다음 2번컴퓨터 연결 된 리스트 확인
        if visited[j]==0: # 1번컴퓨터에 연결 된 2번을 방문했는지? 방문 안했다면 
            dfs(j) # 재귀호출 => 해당 2번 컴퓨터 방문
dfs(1) # 1번부터 방문할꺼니까

print(sum(visited)-1) # 1번컴퓨터를 제외하고 1번 컴퓨터와 연결 된 컴퓨터 갯수 출력

# Bfs : 너비우선 탐색, 자기 자식들을 먼저 탐색
# Dfs : 깊이우선 탐색, 자기 자식의 자식들을 먼저 탐색

