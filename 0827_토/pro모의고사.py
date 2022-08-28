
# answer = [] # 1번문제부터 마지막 문제까지의 정답이 순서대로 들은 배열
# 가장 많은 문제를 맞춘 사람이 누구인지? 

answer = list(map(int, input().split()))

su1 = [1, 2, 3, 4, 5]
su2 = [2, 1, 2, 3, 2, 4, 2, 5]
su3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
c1, c2, c3 = 0, 0, 0
# 여기서 돌려서 리스트에 담고 리스트끼리 비교하려했음..
# 무한대로는 어떻게 하는지? .. 

# 1번수포자
# for i in range(1, len(answer)+1):
#     if i == 6:
#         break
#     su1.append(i)

# 2번수포자 어떻게?? 
# for j in range(2, len(answer)+1):
 
for i in range(len(answer)):
    s1 = i % 5
    s2 = i % 8
    s3 = i % 10
# 비교하는 방법 몰라서 구글링..
    if su1[s1] == answer[i]: 
        c1 += 1 
    if su2[s2] == answer[i]:
        c2 += 1
    if su3[s3] == answer[i]:
        c3 += 1
    
cnt = max(c1, c2, c3)
result = []
if cnt == c1: 
    result.append(1)
elif cnt == c2:
    result.append(2)
else:
    result.append(3)

print(result)


    