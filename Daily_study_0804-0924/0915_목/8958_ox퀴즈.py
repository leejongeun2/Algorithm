
t = int(input())

for _ in range(t):
    m = list(input())
    score = 0 # 연속 점수 쌓는 용도 리셋
    sum_ = 0 # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋
    for i in m:
        if i == 'O':
            score += 1 # o가 있고, 연속이면 1씩 더해줌
            sum_ += score # 계속 점수가 쌓임, 점수 쌓는 용도
        else:
            score = 0 # 연속이 아니면 0
    print(sum_)

    
    