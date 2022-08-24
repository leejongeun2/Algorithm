
s = int(input())
for _ in range(s):
    n, m = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    print(box)
    cnt = 0
    for i in range(m): # 4
        for j in reversed(range(n)): # 5 / 0 ~ 4 # 거꾸로 탐색해야, 밑에서부터 탐색할 수 있음
            if box[j][i] == 1: # 첫번째 4 리스트의 0인덱스 자리가 박스가 있는(1) 경우(왼쪽 하단)
                while True: 
                    if j + 1 == n:# 4+1 = 5가 행5와 같다면, 멈춤 => 세로 길이 넘으면 안되기 때문에 
                        break
                    if box[j+1][i] == 1: # 3, 0 = 1이 아니라서, 브레이크 실행되지 않고 밑으로 넘어감, 밑에도 박스있으면 브레이크이기 때문
                        break
                    box[j][i] = 0 # 
                    box[j+1][i] = 1 # 3, 0 = 1로 바꿔줌 => 박스 내려주고 다시 와일 반복문
                    j += 1 # 이동했으면 j가 커지고 다시 와일문으로 올라감, j가 커지면서 현재것에서 밑에를 탐색
                    cnt += 1 # 이동한 거리 세기 위한 용도
    print(cnt)
