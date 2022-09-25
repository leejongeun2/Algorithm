# 2차원 배열이 주어졌을 때, (i, j)위치부터 (x,y)위치까지 저장되어 있는 수들의 합을 구하는 프로그램
# 이중반복문 학습 

import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split()) 

list2 = [] 
for _ in range(n):
    list2.append(list(map(int, input().split()))) # 이중리스트
# [list(map(int, input().split())) for _ in range(n)]

k = int(input()) # 합을 구할 부분의 갯수 즉, i,j,x,y 한 셋트
for l in range(k): 
    i, j, x, y = map(int, input().split()) # 입력 받아서 각 변수에 저장 됨, 문자열로 저장
    count = 0
    for a in range(i-1, x): # 인덱스이기 때문에 0부터 시작, 범위를 0~1 반복, 행 탐색
        for b in range(j-1, y): # 0~2 반복 => 열탐색
            count += list2[a][b] # 0,0 => 1저장 후 바로 위 for 문으로 돌아감
    print(count)
