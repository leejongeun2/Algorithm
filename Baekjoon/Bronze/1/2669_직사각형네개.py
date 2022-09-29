# 직사각형 네개의 합집합의 면적 구하기

matrix = [[0] * 101 for _ in range(100 + 1)] # 101*101 영행렬을 이중리스트로 생성

# maxtrix = []

# for _ in range(101):
#     maxtrix.append([0]*100)
# print(matrix)

cnt = 0

for i in range(4):
    i, j, x, y = map(int, input().split())
    
    
    for a in range(i, x): # 박스가 밑에서부터 위로 올라감
        for b in range(j, y):
            matrix[a][b] = 1 # 겹치는 부분(이미 있는 1이 있는 것)은 1로 유지할 수 있도록

answer = 0
for row in matrix:
    answer += sum(row) # 각 배열(세로줄)의 합을 구해서 변수에 순차적 저장

print(answer)

    
