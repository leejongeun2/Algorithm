# 모든 알파벳을 종류별로 한개씩 제거한 뒤 알파벳들을 dest의 맨 뒤에 알파벳 순서대로 이어 붙임
# 알파벳 1개인 것 부터 제거 

source = 'bbaabd'
source_lis = list(set(source))


source = 'bbaabd'
source = list(source)
answer = ''
while source:
    temp = []
    resource = []
    for i in source:
        if i not in temp:
            temp.append(i)
        else:
            resource.append(i)
    temp.sort()
    answer += ''.join(temp)
    source = resource
print(answer)


    
    





    

