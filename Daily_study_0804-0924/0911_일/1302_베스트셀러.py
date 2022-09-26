t = int(input()) # 입력 갯수 입력 받고 

cnt = {} # 빈 딕셔너리 생성

for i in range(t): # 입력 갯수만큼 반복
    w = input()
    if w in cnt:
        cnt[w] += 1
    else:
        cnt[w] = 1

max1 = max(cnt.values()) # 딕셔너리의 값 중에 가장 큰 숫자

best = []

for a, b in cnt.items():
    if b == max1:
        best.append(a)

print(sorted(best)[0])

    