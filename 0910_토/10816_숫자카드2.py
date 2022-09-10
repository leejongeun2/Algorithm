
import sys
sys.stdin = open("input.txt")




t = int(sys.stdin.readline())

m = list(map(int, sys.stdin.readline().split()))

t2 = int(input())

n = list(map(int, sys.stdin.readline().split()))

cnt = []

for i in n:
    cnt.append(m.count(i))
print(*cnt)

## 시간 초과 해결 방법 풀이

t = int(sys.stdin.readline())
m = sorted(list(map(int, sys.stdin.readline().split())))
t2 = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))

cnt = {}
for i in m:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1


for i in n:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')

## 시간 초과 해결 방법 풀이 두번째!


import sys
from collections import Counter

M=int(sys.stdin.readline())
list1=list(map(int,sys.stdin.readline().split()))
N=int(sys.stdin.readline())
list2=list(map(int,sys.stdin.readline().split()))

c= Counter(list1)

for i in list2:
  if i in c:
    print(c[i], end=' ')
  else:
    print(0, end=' ')




