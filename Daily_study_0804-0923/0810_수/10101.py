import sys
sys.stdin = open("input1.txt")

a = int(input())
b = int(input())
c = int(input())

if a+b+c == 180:
    if a == b == c == 60:
        print("Equl")
    elif a == b or b == c or a == c:
        print("Iso")
    else:
        print("scalence:")
else: 
    print("Erro")