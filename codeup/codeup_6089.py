# 등비수열
a, r, n = map(int, input().split())

s = a

for i in range(2, n+1):
    s = s*r
print(s)
