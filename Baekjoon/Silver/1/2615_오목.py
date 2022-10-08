# 검은색이 이겼을 때는 1, 흰색이 이겼을 때는 2, 아직 승부가 결정 되지 않았을 경우는 0 
# 이겼을 때, 연속된 다섯개의 바둑알 중에서 가장 왼쪽에 있는 바둑알의 가로죽 번호와, 세로줄 번호를 출력

import sys
sys.stdin = open("input.txt")

n = 19
arr = [list(map(int, input().split())) for _ in range(n)]
 
dx = [1, 1, 0, -1]  # 하(↓), 우하(⬊), 우(➞), 우상(⬈)
dy = [0, 1, 1, 1]    
 
def omok():
    for x in range(n):
        for y in range(n):
            if arr[x][y]: # (0,0)에 존재하는지? 존재하지 않기 때문에 위 y for문으로 => 첫째줄부터 가로방향으로 쭉 탐색
                for i in range(4):
                    nx = x + dx[i] # 2+1 = 3
                    ny = y + dy[i] # 1+0 = 1
                    cnt = 1
 
                    if nx < 0 or ny < 0 or nx >= n or ny >= n: # n=19크거나, 0보다 작으면 아래 실행하지 않음
                        continue
 
                    while 0 <= nx < n and 0 <= ny < n and arr[x][y] == arr[nx][ny]: # 0<=3<19, 0<=1<19, 1(흑돌)==0(비어있음), 돌색이 같을 때 아래 실행(오목이니까)
                        cnt += 1
 
                        if cnt == 5: # 오목이라면? 
                            if 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < n and arr[nx][ny] == arr[nx + dx[i]][ny + dy[i]]:  # 육목 판정 1, 아래
                                break
                            if 0 <= x - dx[i] < n and 0 <= y - dy[i] < n and arr[x][y] == arr[x - dx[i]][y - dy[i]]:  # 육목 판정 2, 위
                                break
                            return arr[x][y], x+1, y+1  # 육목이 아닌 오목이면 return => 인덱스 기준으로 코드짜기 때문에 각 1씩 플러스해줌
 
                        nx += dx[i] # 해당방향으로 같은색돌이 있는 것을 확인했으니까 해당 방향 추가 
                        ny += dy[i]
    return 0, -1, -1  # 승부가 나지 않을 때
 
color, x, y = omok()
if not color: # 칼라가 0일때 
    print(color)
else: # 칼라가 0이 아닐 때 
    print(color)
    print(x, y)