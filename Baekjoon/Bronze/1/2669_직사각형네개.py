# 직사각형 네개의 합집합의 면적 구하기

matrix = [[0] * 101 for _ in range(100 + 1)] # 101*101 영행렬을 이중리스트로 생성

# maxtrix = []

# for _ in range(101):
#     maxtrix.append([0]*100)
# print(matrix)

cnt = 0

for i in range(4):
    i, j, x, y = map(int, input().split())
    
    
    for a in range(i, x): 
        for b in range(j, y):
            matrix[a][b] = 1

answer = 0
for row in matrix:
    answer += sum(row)

print(answer)

    
