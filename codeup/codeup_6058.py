# 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.

a, b = map(int, input().split())

if bool(a)==False and bool(b)==False:
    print("True")
else:
    print("False")


# a, b = input().split()
# c= bool(int(a))
# d= bool(int(b))

# print( not (c or d) ) # or은 두개 값 모두 f일때 f이고, not 하면 반대로 바꿔줌