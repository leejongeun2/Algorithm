# 애너그램
# 두단어 a,b가 주어졌을 때 a에 속하는 알파벳 순서를 바꾸어서 b를 만들 수 있다면 a와 b를 애너그램이라고 함
# 두단어가 애너그램인지 구하는 프로그램 작성
import sys

sys.stdin = open("input1.txt")

t = int(input())
for _ in range(t):
    a, b = input().split()

    x = sorted(list(a)) # 알파벳을 순서대로 오름차순하여 정렬
    y = sorted(list(b))

# print(x)
# print(y)
    if x == y:
        print(f'{a} & {b} are anagrams.')
    else:
        print((f'{a} & {b} are NOT anagrams.'))





