import sys
sys.stdin = open("input1.txt")

lis =  []
word = []

for _ in range(5):
    w = input()
    lis.append(w)
    word.append(len(w))
print(lis)
print(word)

rst = ''
# for i in lis:
#     for j in i:
#         print(j, end="")
for i in range(max(word)): # 길이가 최대 긴 것만큼 반복
    for j in range(5): # 5줄(5 단어)이니까 5번 반복
        if i < word[j]: # 첫번쨰 단어길이가 0보다 더 크면
            rst += lis[j][i] #
print(rst)

