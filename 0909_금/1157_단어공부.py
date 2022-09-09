# 알파벳 대소문자가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지?

# n = input()
# lis = []
# for i in range(len(n)):
#     lis.append(n.count(n[i]))
#     if lis.index(max(lis)):
#         print(n[i])
#     else:
#         print("?")

w = input().lower()
wo = list(set(w))

lis = []

for i in wo:
    cnt = w.count(i)
    lis.append(cnt)

if lis.count(max(lis)) > 1:
    print("?")
else:
    m = lis.index(max(lis))
    print(wo[m].upper())
