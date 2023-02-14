num_list = [] # 리스트 만들고
for i in range(10): # 10개(10번)를 입력받고
    a = int(input())
    if a&42 not in num_list: # 한개씩 입력 받을 때마다, 리스트에 있는지 확인해주고 없다면
        num_list.append(a%42) # 나눈 값을 리스트에 추가
print(len(num_list)) # 리스트의 개수 세기