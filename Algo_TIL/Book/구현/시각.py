# 정수 n이 입력되면 00시 00분 00초 부터 n시 59분 59초까지 의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램
# 가능한 경우의 수를 모두 검사해보는 탐색방법인 완전 탐색방법에 해당
h = int(input())

cnt = 0 
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k): # 'ijk'안에서 '3'이 있는지 확인할 수 있음 즉, 문자열끼리 더하면 'ijk'가 됨
                cnt += 1
print(cnt)