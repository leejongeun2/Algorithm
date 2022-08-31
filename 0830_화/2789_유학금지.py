
# 방법 첫번째
word = list(input())

c = "CAMBRIDGE"


for i in c: # 캠프리지와 입력 받은 문자열을 리스트한 것과 비교
    for j in range(len(word)):
        if i == word[j]:
            word[j] = ''

for i in word:
    print(i, end='')
#============================


# 방법 두번째
string = input()

for i in "CAMBRIDGE":
    string = string.replace(i,"") # 캠프리지를 한개씩 알파벳 별 돌려서, 입력 받은 문자열에 알파벳이 있다면 공백으로 대체
print(string)

#=====================================

# 방법 세번째
c1 = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
result =''
w = input()

for i in w:
    if i not in c1: # not in이란? 포함되지 않는다면
        result += i
print(result)
#=======================

#방법네번쨰

data = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

value = input()
for i in range(len(value)) :
  if value[i] not in data :
    print(value[i], end='')
