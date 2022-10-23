
stack1 = [2, 7]
stack2 = [4, 5]
stack3 = [1]

answer = [] # ['2', '7']

for i in stack1:
    answer.append(str(i))

answer1 = ''.join(answer) #''2''7''

res1 = []

for j in stack2:
    res1.append(str(j))

res11 = ''.join(res1)

res3 = []

for k in stack3:
    res3.append(str(k))

res33 = ''.join(res3)


res2 = '' # 각 숫자가 문자열일 경우 붙음
for l in answer1:
    res2 +=l
for m in res11:
    res2 += m
for e in res33:
    res2 += e
answer = ''


print(res2)



