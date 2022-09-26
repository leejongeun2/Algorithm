import sys
sys.stdin = open("input.txt")

# n = int(input())

# m = list(map(int, input().split()))

# print(min(m), max(m))




# 반복문 이용 
n = int(input())
m = list(map(int, input().split()))
nmax = m[0]
nmin = m[0]

for i in m:
    if i > nmax: # nmax는 맨앞 값이므로, 계속 비교해서 큰 값인 경우 
        nmax = i # nmax를 바꿔줌
    if i < nmin: # 계속 비교해서 작은 값인 경우 바꿔줌
        nmin = i
print(nmin, nmax, end='')