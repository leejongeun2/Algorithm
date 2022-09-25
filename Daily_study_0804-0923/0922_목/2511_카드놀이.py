import sys
sys.stdin = open("input.txt")

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# print(a)
# print(b)

result_a = 0
result_b = 0
result = "D" # 최종 점수가 동점일 때 승패를 가르기 위한 마지막 이긴 사람

for i in range(10):
    # 비길경우
    if a[i] == b[i]:
        result_a += 1
        result_b += 1
    # a가 이길 경우 
    if a[i] > b[i]:
        result_a += 3
        result = 'A'
    # b가 이길 경우
    if a[i] < b[i]:
        result_b += 3
        result = 'B'


if result_a > result_b:
    print(result_a, result_b)
    print("A")

if result_a < result_b:
    print(result_a, result_b)
    print("B")

if result_a == result_b:
    if result == "A":
        print(result_a, result_b)
        print("A")
    if result == "B":
        print(result_a, result_b)
        print("B")
    if result == "D":
        print(result_a, result_b)
        print("D")
        
         
        
        
    

