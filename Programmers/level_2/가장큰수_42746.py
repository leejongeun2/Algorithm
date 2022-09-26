n = list(map(int, input().split()))

m = list(map(str, n))

# print(m, type(m))

m.sort(key=lambda x: x*3, reverse=True)

print(str(int(''.join(m))))