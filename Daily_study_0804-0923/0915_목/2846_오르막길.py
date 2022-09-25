# 오르막길, 내리막길, 평지
# 일정거리마다 높이를 측정, 가장 큰 오르막길의 크기


t = int(input())



m = list(map(int, input().split()))
score = 0
oh = []


for i in range(1, t):
    if m[i] > m[i-1]:
        score+=m[i]-m[i-1] # 오르막길 차를 스코어에 더해줌, 더해주는 것이기 때문에 오르막길 최소값에서 최대값을 구할 수 있음
        if i==t-1: # 4번쨰 돌았을 때, 인덱스 4일때, 턴이 끝났을 때
            oh.append(score) # 오르막길 차를 리스트에 넣어줌
    else:
        oh.append(score) # 증가가 아닐 경우 흐름을 끊어야 되기 떄문에 점수를 넣어줌
        score=0 # 그리고 점수를 0으로 초기화

        

print(max(oh)) #

