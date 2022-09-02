# 숫자를 거꾸로 읽음




n, m = input().split()
nr = int(n[::-1])
mr = int(m[::-1])


print(max(nr,mr))