# 시작 값(a), 등차의 값(d), 몇 번째 수 인지를 의미하는 정수(n)가
# 공백을 두고 입력된다.(모두 0 ~ 100)

# n번째 수를 출력한다.

a, d, n = map(int, input().split())

s = a
for i in range(2, n+1):
    s+=d
print(s)

a,d,n=map(int, input().split())

print(a+d*(n-1)) # 등차수열의 일반항 공식