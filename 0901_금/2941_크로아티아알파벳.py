# c = input()

# dic = {"č":"c=", "ć":"c-", "dž":"dz=", "đ":"d-", "lj":"lj", "nj":"nj", "š":"s=", "ž":"z="}
# result= ''
# for i in c:
#     if i not in dic:
                


# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input()

# for i in croatia :
#     word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
# print(len(word))

#========================

word = input()
c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for i in range(len(c)):
    if c[i] in word: #입력 받은 단어안에 크로아티아 문자가 포함되어있는지?
        w_count = word.count(c[i]) #입력 받은 단어 안에 크로아티아 첫번쨰 문자가 몇개있는지?
        word = word.replace(c[i], " ")
        count += w_count #입력 받은 단어 안에 크로아티아 문자가 몇개있는지 누적해줌
word = word.replace(" ", "") #공백을 공백 없애는 것으로 바꿈
count += len(word)

print(count) # 크로아티아 대체 문자들이 얼마나 있는지 탐색 후, 있다면 
# 한개씩으로 만들어서 카운트에 저장 후 남은 문자열과 더해줌
# 특이점은 w_count를 사용하여 몇개 있는지 확인 후 여러개가 있다면 카운트에 더해줌

