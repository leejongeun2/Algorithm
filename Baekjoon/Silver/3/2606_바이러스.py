# 1번 컴퓨터가 바이러스 걸렸을 때, 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램 작성

n = int(input())
link = int(input())

network = []

for _ in range(n+1):
    network.append([]*(n+1)) #인덱스 기준이니 1~7번이 들어갈 9자리 빈 리스트 생성

# print(network)
for i in range(link):
    a, b = map(int, input().split())
    network[a].append(b) # 1의자리에 2를 넣어줌
    network[b].append(a) # 2의자리에 1을 넣어줌 

visited = [0]*(n+1) # 방문 체크해주는 곳

def dfs(v):
    visited[v]=1
    for j in network[v]:
        if visited[j]==0:
            dfs(j)
dfs(1)
print(sum(visited)-1)


