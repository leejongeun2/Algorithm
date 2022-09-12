t = int(input())

cnt = {}

for i in range(t):
    w = input()
    if w in cnt:
        cnt[w] += 1
    else:
        cnt[w] = 1

max1 = max(cnt.values())

best = []

for a, b in cnt.items():
    

if cnt.count(max(cnt.keys())) > 1:
    print(cnt)
else:
    print(max(cnt.keys()))

    