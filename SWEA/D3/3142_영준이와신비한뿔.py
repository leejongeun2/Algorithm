t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    one = 0
    while m *2 + one*1 > n:
        m -= 1
        one += 1
    print(f'#{_+1} {one} {m}')
    
    