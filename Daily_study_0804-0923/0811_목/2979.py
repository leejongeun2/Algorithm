# 트럭 주차

# 총 트럭 세대 
# 트럭을 주차하는데 비용이 얼마나 드는지? 
# 주차하는 트럭의 수에 따라 주차 요금을 할인해줌
# 트럭 한대를 주차할 떄는 1분에 한대당 a원
# 트럭 두대를 주차할 때는 1분에 한대당 b원
# 트럭 3대를 주차할 때는 1분에 한대당 c원
# c<b<a

import sys

sys.stdin = open("input2.txt")

a, b, c = map(int, input().split())

table = []

for _ in range(3):
    n = list(map(int, input().split()))
    table.append(n)
    

# print(table)
m = max(table[0][1], table[1][1], table[2][1]) # 떠난 시간 3개를 맥스 함수로 비교해 가장 마지막으로 떠난 트럭의 시간을 구함
parking = [0]*(m-1)

for i in table:
    for j in range(i[0]-1, i[1]-1):
        parking[j] += 1

    fee = 0
    for car in parking:
        if car == 1:
            fee += a
        elif car == 2:
            fee += 2 * b
        elif car == 3:
            fee += 3 * c
    

print(fee)




