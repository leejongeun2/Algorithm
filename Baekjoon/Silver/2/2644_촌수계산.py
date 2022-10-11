from collections import deque

def bfs(s):
    queue=deque([s])
    visited[s]=True

    while queue:
        v=queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                res[i]=res[v]+1 # 연결 되어있는 인덱스자리의 숫자는 기준 노드자리 숫자에서 +1
                visited[i]=True

n=int(input())
A,B=map(int,input().split()) # 촌수계산해야하는 7번과 3번이주어짐
m=int(input())

graph=[[] for _ in range(n+1)]
visited = [False] * (n + 1)
res=[0]*(n+1)


for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(A)

if res[B]>0:
    print(res[B])
else:
    print(-1)
 