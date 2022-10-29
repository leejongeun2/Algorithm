# 주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과 만들 수 있는 색의 가짓 수를 계산

r, g, b = map(int, input().split())

cnt = 0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            cnt = cnt + 1

print(cnt)