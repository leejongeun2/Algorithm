
import sys
sys.stdin = open("14467_input.txt")

cow = [[-1]*10, [0]*10] # 이차원배열
print(cow)

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    if cow[0][n-1] == -1:
        cow[0][n-1] = m
        continue
    if cow[0][n-1] != m:
        cow[0][n-1] = m
        cow[1][n-1] += 1
        continue

print(sum(cow[1]))