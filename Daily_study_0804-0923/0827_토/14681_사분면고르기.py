n = int(input())
m = int(input())

if n < 0 and m >0:
    print("2")
elif n > 0 and m>0:
    print("1")
elif n>0 and m<0:
    print("4")
else:
    print("3")