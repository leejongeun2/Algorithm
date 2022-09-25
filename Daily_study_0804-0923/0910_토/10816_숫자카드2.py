
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

cnt = {} # 빈 딕셔너리 생성
for i in m: # 탐색하는 숫자 리스트를 오름차순으로 순회
    if i in cnt: # 탐색하는 숫자가 딕셔너리에 있다면
        cnt[i] += 1 # 해당숫자의 밸류값에 1 플러스
    else: # 탐색하는 숫자가 딕셔너리에 없다면
        cnt[i] = 1 # 밸류값에 1 넣음


for i in n: # 갯수 셀 숫자들 순회
    if i in cnt: # 딕셔너리에 있으면
        print(cnt[i], end=' ') #해당 키의 밸류값 출력
    else: # 없으면 0으로 출력
        print(0, end=' ')

## 시간 초과 해결 방법 풀이 두번째!


import sys
from collections import Counter

M=int(sys.stdin.readline())
list1=list(map(int,sys.stdin.readline().split()))
N=int(sys.stdin.readline())
list2=list(map(int,sys.stdin.readline().split()))

c= Counter(list1) # 리스트 안에 있는 숫자들에 대한 빈도수를 딕셔너리 형태로 만드는 모듈

for i in list2:
  if i in c:
    print(c[i], end=' ')
  else:
    print(0, end=' ')




