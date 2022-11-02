# 3명이 같은 날 가입/등업하고, 각각 3일마다, 7일마다, 9일마다
# 한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 함께 문제를 풀게 된다.


a, b, c = map(int, input().split())

d = 1
while d%a!=0 or d%b!=0 or d%c!=0 : # a, b, c중 나머지가 0이 아닐 동안 반복, 0이면 날짜 추가 불가 
  d += 1

print(d)

a,b,c=map(int,input().split())

i=0
while True:
    i = i + 1

    if i % a == 0 and i % b == 0 and i % c == 0:
        print(i)
        break