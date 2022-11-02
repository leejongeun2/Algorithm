# 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

n = int(input())

a = map(int, input().split()) # 정수형으로 꼭 비교해줘야함 왜냐, 정수형이 아닌 경우 각각 문자열이 되고 맨 앞 숫자롤 min이 계산됨

m = min(a)

print(m)