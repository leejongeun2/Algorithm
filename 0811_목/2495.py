import sys

sys.stdin = open("input.txt")


for _ in range(3):
    s = str(input())
    max_ = 1 # 연속된 숫자가 몇개인지 카운트하는 변수
    cnt = 1 # 다음에도 연속 된 숫자가 있을 수 있으니, 그것을 카운트하고 max_변수보다 작다면 아래 조건에서처럼 1로 초기화
    for i in range(1, len(s)): #문자열 길이만큼 탐색
        if s[i]==s[i-1]: # 앞의 인덱스값과 이전 인덱스값이 같은지 비교
            cnt += 1 # 같다면 1 추가
        else: # 같지 않다면
            max_ = max(cnt, max_) # cnt 변수와 비교해서 더 큰 값으로 max_변수 갱신
            cnt = 1 # 같지 않다면 초기화
    max_ = max(cnt, max_)
    print(max_)
