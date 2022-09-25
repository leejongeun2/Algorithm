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
    for j in range(i+1,9): # # 1~8 인덱스 각 인덱스 비교, 범위 초과하면 밑에 두번쨰 if문으로 감
        if 100 == total - (list1[i] + list1[j]): # 7명의 키가 100이니까 총 난쟁이들 9명 합에서 두명을 빼면 100이 나와야함
            # if조건에 해당되지 않는 것이 초반에는 많기 때문에 해당 되지 않으면 15행 for문이랑 왔다갔다함
            num1,num2 = list1[i], list1[j] # 두명 값을 추출

            list1.remove(num1) # 두 명 값 제거
            list1.remove(num2)
            list1.sort()

            for i in range(len(list1)): # 두명 제외한 것 출력
                print(list1[i])
            break

    if len(list1) < 9: # 첫번째 for문에 해당함, 두번째 for문 다 되면 이쪽으로 가서 한번 더 확인
        # ist1 의 길이가 9보다 작아야함 => 즉, 위에서 값 제거가 안되면 다시 맨 처음 for문으로 감
        # 즉, 제거가 되면 여기서도 브레이크 해줌
        break
