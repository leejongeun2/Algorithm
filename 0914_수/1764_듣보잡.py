# a, b가 주어질 때 교집합 구하기
# 첫째줄에 듣도 못한 사람의 수 n
# 보도 못한 사람의 수 m

import sys
sys.stdin = open("input1.txt")

n, m = map(int,input().split())

a = set()

for i in range(n):
    d = input()
    a.add(d)


    
b = set()
for j in range(m):
    bb = input()
    b.add(bb)

result = sorted(list(a&b))

print(a)

print(len(result))

for i in result:
    print(i)