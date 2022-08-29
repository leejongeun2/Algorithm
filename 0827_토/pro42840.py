
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
        c1 += 1 # 수포자1이 맞추면 체크
    if su2[s2] == answer[i]:
        c2 += 1 # 수포자2가 맞추면 체크
    if su3[s3] == answer[i]:
        c3 += 1 #수포자3이 맞추면 체크
    
cnt = max(c1, c2, c3) #체크 된 것 중 제일 큰 것
result = []
if cnt == c1: # 제일 큰 것이 1이라면
    result.append(1) #결과에 1추가
if cnt == c2:
    result.append(2) #결과에 2 추가
if cnt == c3:
    result.append(3) # 모든 조건문 탐색을 위해 다 if문으로 써줌

print(result)


    