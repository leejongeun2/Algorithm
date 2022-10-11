from collections import deque

def bfs(s):
    queue=deque([s])
    visited[s]=True

    while queue:
        v=queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                res[i]=res[v]+1
                visited[i]=True

n=int(input())
A,B=map(int,input().split())
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
 