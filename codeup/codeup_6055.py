# 2개의 정수값이 입력될 때, 그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램

a, b = map(int, input().split())

if bool(a) or bool(b) == True:
    print("True")
else:
    print("False")