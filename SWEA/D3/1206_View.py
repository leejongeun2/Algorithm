# 왼쪽과 오른쪽 창문을 열었을 때, 양쪽 모두 거리 2이상의 공간이 확보될 때 조망권이 확보 됨
# 조망권이 확보 된 세대 수를 반환하는 프로그램
# 한 빌딩을 기준으로 직접 양쪽 2개 빌딩의 높이 차를 계산해보면 쉽게 조건을 찾아 풀 수 있다. 

# height = int(input())

# for _ in range(10):
#     print(_)


for order in range(1, 10 + 1): # 테스트 케이스
    n = int(input()) # 건물의 개수, 예시: 12
    gangnam = list(map(int, input().split())) # n개의 건물 높이, 예시 0 0 3 5 2 4 9 6 4 6 0 0
    count = 0  # 정답을 출력할 변수
    for i in range(2, len(gangnam) - 2):  # 초기 양쪽 2개씩 0을 제외한 인덱스를 돈다.(양쪽 두개는 0이기 때문에 예시 경우 2~10까지돌음)
        max_result = []  # i를 기준으로 양쪽 2개씩 총4개의 조망권을 저장할 리스트 선언
        for j in range(i - 2, i + 3):  # 양쪽으로 2칸을 확인해야 하기 때문 => 오른쪽 왼쪽 2칸이상 조망권이 확보되어야 하기 때문 예시 경우, (0~5)
            if i == j:  # 만약 인덱스가 본인이라면(비교할 대상이 자기자신) 밑에 조건을 실행할 필요가 없으므로 continue
                continue
            result = gangnam[i] - gangnam[j]  # 우선 조망권을 받을 수 있는 층수를 계산하여(0자리 높이와 3자리 높이 차)
            if result < 0:  # 그 값이 음수라면 양옆 각 두개의 건물 중 조망권이 확보된 집이 없으므로
                max_result = []  # 리스트를 다시 비워주고
                break  # 반복문 탈출
            max_result.append(result)  # 조망권 값들을 리스트에 추가해준다.

        if max_result:  # 만약 리스트가 비어있지 않다면
            count += min(max_result)  # 조망권 확보가 가능한 최솟값을 출력변수에 더해준다.

    print(f'#{order} {count}')