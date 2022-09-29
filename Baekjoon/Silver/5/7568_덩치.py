import sys

t = int(input())

lis = []
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    lis.append((n, m))

for i in lis: # 첫번째 사람부터 나머지 사람과 비교
    rank = 1 # 초기값 1로 셋팅 => 제일 크면 1등이 되는 것임
    for j in lis: # 다른사람들과 비교 
        if i[0] < j[0] and i[1] < j[1]: # 첫번째는 자기자신과 비교되며, 다른 사람이 키, 몸무게 모두 커야지 자신의 등수가 +1되어 밀려나게 됨
            rank += 1 # 다른사람과 비교 시, 다른사람이 크다면, 등수 +
    print(rank, end = " ")
