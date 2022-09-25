import sys

sys.stdin = open('input.txt')

t = int(sys.stdin.readline())
m = sorted(list(map(int, sys.stdin.readline().split())))
t2 = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))

print(t)
print(m)
print(t2)
print(n)