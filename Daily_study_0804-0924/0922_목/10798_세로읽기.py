import sys
sys.stdin = open("input1.txt")

lis =  []
word = []

for _ in range(5):
    w = input()
    lis.append(w)
    word.append(len(w))


rst = ''
# for i in lis:
#     for j in i:
#         print(j, end="")
for i in range(max(word)): # 길이가 최대 긴 것만큼 반복
    for j in range(5): # 5줄(5 단어)이니까 5번 반복
        if i < word[j]: # 해당하는 세로줄 인덱스 < 해당하는 자릿수라면 즉, 5번째 세로줄(인덱스4) < 6 해당되며,5번째 세로줄(인덱스4) < 4
            rst += lis[j][i] #
print(rst)

