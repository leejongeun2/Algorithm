registered_list = ["cow","cow1","cow2","cow3","cow4","cow5","cow6","cow7","cow8","cow9","cow9"]
registered_list_set = set(registered_list)
new_id = "cow"

answer = ''
temp = ''

if new_id in registered_list_set:
    for i in new_id:
        if i in "0123456789":
            temp += i 
        else: 
            answer += i
    if len(temp) > 0:
        while answer+temp in registered_list_set:
            temp = int(temp)
            temp += 1
            temp = str(temp)
    else: 
        temp = "1"
        if answer+temp in registered_list_set:
            while answer+temp in registered_list_set:
                temp = int(temp)
                temp += 1
                temp = str(temp)
    answer = answer+temp
else:
    answer += new_id
print(answer)


# 포함하지 않으면 출력 
# 포함하면 +1 , 그것도 포함하면 증가시키고, 포함하지 않을때까지 증가하기
