# 알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지 숫자로 변환하여
# 출력하라

import sys
sys.stdin = open("input.txt")

n = input().split()

# for i in range(len(n)):
#     print(ord(n[i])-64, end=' ')

print(n, type(n))

