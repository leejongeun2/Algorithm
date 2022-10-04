# 1004 아침 풀 예정

doc = input()
word = input()
count = 0
i = 0
while i <= len(doc) - len(word):
    if doc[i:i + len(word)] == word:
        count += 1
        i += len(word) # 단어의 길이만큼 인덱스를 더해주고
    else:              # 찾지 못하면
        i += 1         # 1만큼 인덱스를 더해줌
print(count)