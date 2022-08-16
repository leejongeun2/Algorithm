# w, k 우열을 정해야됨
# 10명씩 콘테스트에 참여, 10명중 득점이 높은 사람에서 3명의 점수를 합산한 점수가 각 대학의 득점
# 두 개 대학 참가자의 점수 데이터가 주어짐
# 각 대학의 점수를 계산하는 프로그램을 작성

import sys
sys.stdin = open("input.txt")

# a_list = []
# for _ in range(10):
#     s = int(input())
#     a_list.append(s)
#     set(a_list)

#     result = sorted(a_list, reverse=True)
#     s_result = []
#     for i in result:
#         if i > i+1:
#             s_result.append(i)
#         if 
    
#     print(s_result)

w = []
k = []

for i in range(0, 10):
    a = int(input())
    w.append(a)
for i in range(0,10):
    b = int(input())
    k.append(b)
w.sort(reverse=True)
k.sort(reverse=True)
wsum = 0
ksum = 0
for i in range(0, 3):
    wsum += w[i]
    ksum += k[i]
print(wsum, ksum)




    
