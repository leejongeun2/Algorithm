# 모든 알파벳을 종류별로 한개씩 제거한 뒤 알파벳들을 dest의 맨 뒤에 알파벳 순서대로 이어 붙임
# 알파벳 1개인 것 부터 제거 

source = 'bbaabd'
source_lis = list(set(source))


# while len(source) > 0:

# while len(source_lis)>0: # 소스에 문자열이 있을 때
#     # for i in range(source):
#     #  if source.count(i)>1:
#     #     dest.append(i)
lis = []
for i in source_lis: # b, d, a 
    answer = ''
    if source.count(i) > 1 :
        lis.append(i)
        
    elif source.count(i) == 1:
        answer += i
no_set_lis = list(set(lis))
print(no_set_lis)
print(answer)


    
    





    

