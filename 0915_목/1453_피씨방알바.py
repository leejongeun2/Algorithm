t = int(input())

dic = {}


m = list(map(int, input().split()))

for i in m:
    if i in dic:
        dic[i] += 1  
    else: 
        dic[i] = 1

# lis = [k for k, v in dic.items() if v>1]

lis = []
for k, v in dic.items():
    if v > 1:
        lis.append(v)


if len(lis) > 0:
    print(sum(lis)-len(lis))
else:
    print(0)








# print(dic.items())






