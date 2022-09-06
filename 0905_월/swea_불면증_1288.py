# t = int(input())

# for _ in range(t):
#     n = int(input())
#     lis = []

#     while True:
#         lis.append(i*n)
#     print(lis)
import sys
sys.stdin = open("input.txt")

t = int(input())

for _ in range(t):
    n = input() # 1 문자열로 입력받음
    value = int(n) # 정수형으로 바꿔줌
    data = [0]*10 # 0이 10개인 리스트 만들어줌
    while True: # 범위 없이 반복
        for i in range(len(n)): # 문자열 길이만큼 반복 즉, 9까지는 1번반복
            data[int(n[i])] += 1 #문자열의 0번째의 값을 정수형으로 바꿔서, 해당 자리값에 1을 추가해줌
        if not data.count(0): # 추가해준 것에서 0이 없을 때 출력하고 반복문 멈춤
            print(f'#{_+1} {int(n)}')
            break

        n = str(value+int(n)) # 데이터 리스트에 0이 아직 있다면 입력 받은 정수형끼리 더해서 숫자를 하나씩 증가시켜 문자열로 만들어줌
