# 첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
# 두 번째 줄에 놓을 수 있는 막대의 개수(n)
# 세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.

h, w = map(int, input().split())
n = int(input())

zeros = [[0] * w for _ in range(h)] # h범위로 큰 리스트가 만들어지고, w의 범위로 각 큰 리스트의 요소 안에 리스트가 생김

# zeros = []
# for _ in range(h):
#     zeros.append([0]*w) 0이 w만큼 있는 리스트를 zeros리스트에 추가

for i in range(n):
    l, d, x, y = map(int, input().split())

    for j in range(l):
        if d == 0:
            zeros[x-1][y-1+j] = 1 # 인덱스 기준이 아니니까 -1 해줌, 가로니까 하나씩 막대길이 만큼 오른쪽으로 넓혀감
        else:
            zeros[x-1+j][y-1] = 1 # 세로니까 아래쪽으로 넓혀감

for i in range(h):
    for j in range(w):
        print(zeros[i][j], end=' ')
    print(end='\n')
