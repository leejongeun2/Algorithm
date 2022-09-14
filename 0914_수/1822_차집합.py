# 몇개의 자연수로 이루어진 두 집합 a, b에서 a에는 속하면서 b에는 속하지 않는 모든 원소를 구하는 프로그램
# 첫째 줄에는 집합 a의 원소의 개수 n(a)와 집합 b의 원소의 개수 n(b)

import sys
sys.stdin = open("input.txt")


a, b = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(a-b))
print(*sorted(list(a-b)))
