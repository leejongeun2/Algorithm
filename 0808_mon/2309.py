# 일곱난쟁이
# nan = []

# for i in range(9):
#     nan.append(int(input()))

# print(nan)

list1 = [int(input()) for i in range(9)]

total = sum(list1)
# 중복 없이 한칸씩 확인해아하니, 이중 반복문으로 각 인덱스 값 확인(0, 1), (0, 2), (0, 3), (0, 4) ...
# 두번째 (1, 2), (1, 3)...
for i in range(9): # 0~8 인덱스 
    for j in range(i+1,9): # # 1~8 인덱스 각 인덱스 비교
        if 100 == total - (list1[i] + list1[j]): # 7명의 키가 100이니까 총 난쟁이들 9명 합에서 두명을 빼면 100이 나와야함
            num1,num2 = list1[i], list1[j] # 두명 값을 추출

            list1.remove(num1) # 두 명 값 제거
            list1.remove(num2)
            list1.sort()

            for i in range(len(list1)): # 두명 제외한 것 출력
                print(list1[i])
            break

    if len(list1) < 9:
        break
