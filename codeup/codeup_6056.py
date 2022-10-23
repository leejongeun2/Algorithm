# 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성

a, b = map(int, input().split())

if bool(a) ^ bool(b) == True: # 참거짓이 서로 다를 때(0이 false, 1이 true), 0 ^1=1, 1^0=1
    print("True")
else:
    print("False")

print((bool(a) and (not bool(b))) or ((not bool(a)) and bool(b)))
# a일때 트루이고, b는 false, 또는 a는 false이고 b는 true임

# 참 거짓이 서로 다를 때에만 True 로 계산하는 논리연산을 XOR(exclusive or, 배타적 논리합) 연산이라고도 부른다.