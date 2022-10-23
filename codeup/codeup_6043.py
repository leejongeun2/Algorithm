# 실수 2개를 입력 받아, 앞에것을 뒤에것으로 나누 값 출력
# 이때, 소숫점 넷째자리에서 반올림

a,b=input().split()
a=float(a)
b=float(b)
c = a/b

print(format(c, ".3f"))