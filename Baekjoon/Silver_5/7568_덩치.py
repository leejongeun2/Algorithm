t = int(input())

lis = []
for _ in range(t):
    n, m = list(map(int, input().split()))
    list.append(n, m)

for i in lis:
    rank = 1
    for j in lis:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")
