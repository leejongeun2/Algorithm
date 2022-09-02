# 불의의 교통사고를 당한 당신은 얼마 후 자신의 인식 속에서 모음이 사라진 것을 알게되었다. 
# 단어를 입력 받으면 모음이 아닌 것을 빼고 출력 

# t = int(input())

# mo = ['a', 'e', 'i', 'o', 'u']

# for _ in range(t):
#     result =''
#     a = list(input())
#     for i in a: # a의 문자열을 하나씩 탐색
#         if i not in mo:
#             result += i
#     print(f'#{_+1} {result}')
        

#=====================

# mo = 'aeiou'
# word = list(input())

# for _ in mo:
#     for i in range(len(word)):
#         if _ == word[i]:
#             word[i] = ''

# for j in word:
#     print(j, end='')

#==========================

# mo = input()

# for i in "aeiou":
#     mo = mo.replace(i, "")
# print(mo)

#==========================

mo = ['a', 'e', 'i', 'o', 'u']
word = input()

for i in range(len(word)):
    if word[i] not in mo:
        print(word[i], end='') # 





