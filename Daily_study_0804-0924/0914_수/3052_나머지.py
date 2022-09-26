# 수 10개를 입력 받은 뒤, 이를 42로 나눈 나머지를 구한다. 
# 서로 다른 값이 몇 개 있는지 출력하는 프로그램 작성

lis = []

for i in range(10):
    a = int(input())
    lis.append(a%42)
print(len(set(lis)))

