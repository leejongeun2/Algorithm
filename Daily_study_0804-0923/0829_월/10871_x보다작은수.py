n, m = map(int, input().split())
num = list(map(int, input().split()))
list1 = []
for i in num:
    if i < m :
        list1.append(i)

print(*list1)