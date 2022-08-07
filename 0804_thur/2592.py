# 대표값
# 평균, 최빈수 구하기 
# 첫쨰 줄부터 열번째 줄까지 하나씩 자연수가 주어짐 => 첫째줄 평균 출력, 두번째 줄 최빈 값 출력(최빈 값이 둘 이상일 경우 그 중 하나만 출력)

data = []

for _ in range(10): # 반복문 통해 10번 반복 입력 받아 데이터 리스트에 넣음
    data.append(int(input()))

print(sum(data) // 10) # 데이터 리스트에 담겨있는 값들의 합을 구해 10으로 나눈 값 즉, 평균을 출력하고 

print(max(data, key = data.count)) #데이터 리스트에 담겨있는 값 중복 갯수 중 가장 큰 것
# 데이터 리스트와, 데이터 리스트에 담겨 있는 숫자를 센 것 중에 큰 값 구하기 
# max : 둘 중 큰 것 또는 key로 함수를 지정해서 해당 함수에 따라 가장 큰 것을 반환 => len 도 가능
# max key 기능: key 매개변수에 지정된 함수를 기반으로 iterable을 비교할 수도 있음






