# 다장조는 c d e f g a b c 총 8개 음으로 이루어져있음
# 1~8까지 매칭이 됨

n = list(map(int, input().split()))

x = sorted(n)
m = sorted(n, reverse=True)

if n == x:
    print("ascending")
elif n == m:
    print("descending")
else:
    print("mixed")



