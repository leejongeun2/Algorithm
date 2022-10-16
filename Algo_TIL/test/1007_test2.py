# 검색 엔진은 유사한 단어를 검색하는 알고르짐에 대해 훈련
# 소스와 타켓이라는 두 단어가 주어지면 순열 순서로 정의 된 인덱스 시퀀스에 따라, 
# 문자열 소스에서 문자가 하나씩 제거됨
# order = [ ], 길이 n
# 소스 : "abbabaa", 타겟: "bb", 제거순서 order=[7,1,2,5,4,3,6]간주, 굵게 표시 된 문자는 하위 시퀀스, -는 제거 된 문자
# 제거 몇개까지 가능한지

source = 'hkbid'
target = 'kd'
order = [3,4]
cnt = 0
for i in order:
    i -= 1
    source = list(source)
    source[i] = '_'
    source = ''.join(source)
    answer = ''
    for i in source:
        if i != '_':
            answer += i
    if answer.count(target) > 0:
        cnt += 1
    
print(cnt)

            




