


a = list(map(int, input().split()))


c = []

for i in range(3):
    b = list(map(int, input().split()))
    c.append(b)

result= []
for i in c:
    a1 = a[i[0]-1:i[1]]
    a2 = sorted(a1)
    # print(a2)
    a3 = a2[i[2]-1]
    result.append(a3)
print(result)

    