# 총 n개의 정수가 주어졌을 때, 특정 정수 한개가 몇새인지 구하는 프로그램




n = int(input())

# for _ in range(len(n)):
m = list(map(int, input().split()))
v = int(input())

result = m.count(v)
print(result)

### 두번재 방법

N = int(input())
l = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in l:
    if i == v:
        cnt += 1
        
print(cnt)


