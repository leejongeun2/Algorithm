# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력

from re import I


n = int(input())

for i in range(n):
    n = 2**i
    print(n, end='')
