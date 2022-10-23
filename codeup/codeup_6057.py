# 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.

a, b = map(int, input().split())

# if bool(a) ^ bool(b) == True: # 참거짓이 서로 다를 때, (0이 false, 1이 true), 0 ^1=1, 1^0=1
#     print("False")
# else:
#     print("True")

print(bool(a)==bool(b))