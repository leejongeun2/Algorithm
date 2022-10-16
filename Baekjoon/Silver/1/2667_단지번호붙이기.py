# 정사각형 모양의 지도에서 1은 집이 있는 곳, 0은 집이 없는 곳 
# 이 지도를 가지고 연결 된 집의 모임인 단지 정의 
# 단지에 번호를 붙임
# 연결 되어있는 것은 좌우, 아래위를 말함(대각선x)
# 단지 수 출력(배추, 그림 덩이랑 같은 문제), 집의 수(그림의 크기랑 같은 문제)오름 차순
n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1] # 오른, 왼, 아래, 위
dy = [1, -1, 0, 0]


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1 # 배열에 아파트가 몇개있는지
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False


count = 0
result = 0

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True: # 0이면 false이므로, 해당 조건에 해당 안됨
            num.append(count) # Count를 num이라는 빈 리스트에 더해줌
            result += 1 
            count = 0

num.sort()
print(result) # 총 단지 수
for i in range(len(num)): # 단지 내 집의 수를 오름차순
    print(num[i])