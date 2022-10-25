# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

n = int(input())
s = 0
for i in range(1, n+1) :
  if i%2==0 :
    s += i
print(s)
