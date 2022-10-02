t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    r = n//m # 뿔을 동물의 수로 나눔
    h = m-3 # 동물의수에서 위의 나눈 값을 뺌
    result = 2*r + 1*h # 투혼과 r(몫)을 곱하고 + 유니와 h값을 더한값
    while result > n: #더한값이 뿔의 수보다 크면 
        2*(r-1)+1*(h+1) # 투혼마리를 줄이고, 유니를 +1함
    while result < n: # 계산하여 뿔과 같다면 출력
        2*(r+1)+1*(h-1) # 투혼 마리수 늘리고, 유니를 -1함
    while result ==n:
        print(h, r)