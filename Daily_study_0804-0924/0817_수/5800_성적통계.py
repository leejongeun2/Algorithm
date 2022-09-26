n = int(input())
for j in range(n):
    a = list(map(int, input().split()))
    a.remove(a[0])
    a.sort()
    lis = []
    print('Class', j+1)
    
    for i in range(len(a)-1):
        lis.append(a[i+1] - a[i])
    print(f'Max {max(a)}, Min {min(a)}, Largest gap {max(lis)}')