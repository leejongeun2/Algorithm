# 어떤 수가 주어졌을 때, 그 수의 모든 자리 수가 역순이 된 수를 얻을 수 있다.
# 두 역순 숫자의 합의 역순




# x, y = map(int, input().split())

# x1 = int(str(x)[::-1])
# y1 = int(str(y)[::-1])
# sum1 = x1+y1
# sum2 = int(str(sum1)[::-1])
# print(sum2)

s = 'abcde'
print(''.join(reversed(s)))  # 'edcba'