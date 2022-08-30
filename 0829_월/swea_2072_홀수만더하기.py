import sys
sys.stdin = open("input.txt")

t = int(input())

for _ in range(t):
    m = list(map(int, input().split()))
    list1 = [] # 리스트를 테스트케이스 안에 숫자리스트를 입력 받은 후 빈리스트를 넣어줘야 함, 왜냐? 밑에서 for 문을  또 돌려서 체크해주기 때문
    # 만약 테스트케이스 밖에 있다면, 계속 쌓임, 안에 있어서 입력 받을 때마다 반복되어 초기화 되는 것임
    for i in m:
        if i%2 == 1:
            list1.append(i)
    print(f'#{_+1} {sum(list1)}')
    
