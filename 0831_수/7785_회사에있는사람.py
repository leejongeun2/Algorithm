# N = int(input())
# pe = {}

# for _ in range(N):
#   p, c = input().split()

#   if c == 'enter':
#     pe[p] = 'enter'
#   else:
#     if pe[p]:
#       del pe[p]

# for people in sorted(pe, reverse=True):
#   print(people)

n = int(input())
dic = {}
for _ in range(n):
    a, b = input().split()
    dic[a] = b # 딕셔너리 박스에 키, 값을 지정

lis = [k for k, v in dic.items() if v == 'enter'] 
# 딕셔너리로 k,v받고(dic.items),k를 lis에 리스트화해줌, 단 v가 enter인 
# lis = []
# for k, v in dic.items():
#     if v == 'enter':
#         lis.append(k)

lis.sort()
lis.reverse()
print(*lis, sep = '\n') #리스트 풀고, 엔터로 분리해줌