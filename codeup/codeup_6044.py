# 정수 두개를 입력 받아, 합, 차, 곱, 몫, 나머지, 나눈 값 

a,b=input().split()
a = int(a) # 꼭 정수로 바꿔주기!! 
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b, ".2f")) # round, 2도 반올림해줌