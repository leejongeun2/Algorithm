n = int(input())

for i in range(1, n+1): #1~10까지 i로 출력됨
    if n%(i)==0:
        print(i, end = " ")