# 보물의 절반을 보상으로 파일 정리를 요청함
# 파일을 확장자 별로 정리해서 몇개씩 있는지 
# 보기 편하게 확장자들을 사진으로 정렬

t = int(input())

dic = {}

for _ in range(t):
    m = input().split('.')[1]
    if m not in dic:
        dic[m] = 1
    else:
        dic[m] += 1

sort_dic = sorted(dic.items())

for k, v in sort_dic:
    print(k, v)

