# 딕셔너리 풀이법

t = int(input())

for i in range(t):
    n = int(input())
    m = list(map(int, input().split()))

    dic = {}
    for i in m:
        if i in dic:
            dic[i] += 1
        else: 
            dic[i] = 1
    max_ = max(dic.values())
    key_ = [k for k, v in dic.items() if v==max_]

    if len(key_) == 1:
        print(f'#{n} {key_[0]}')
    else:
        print(f'#{n} {max(key_)}')
    
 
    
    


# t = int(input())

# for _ in range(t) :
#     tc = int(input())
#     score = list(map(int, input().split()))
#     data = [0] * 1001 #1번부터 1001번까지의 범위가 있으니까 0으로 된 배열 생성

#     for i in score : # 입력 받은 값 탐색하여 
#         data[i] += 1 # 해당하는 자리 즉, 1이면 1의 자리 체크

#     max_value = max(data) # 데이터 배열의 최대값
#     result = []
#     for i in range(len(data)) : 데이터 배열 길이만큼 탐색
#         if data[i] == max_value : 데이터 배열 앞에서부터 하나씩 탐색할 때 최대값인 경우 
#             result.append(i) 빈 리스트에 추가 

#     print('#%d %d' % (tc, max(result))) 빈 리스트 최댓값