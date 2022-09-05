# 자연수가 있을 떄, 분해합은 n과 n을 이루는 각 자리수의 합을 의미한다, 
# 245인 경우, 245+2+4+5=256(245의 생성자)

t = int(input())

result = 0
for i in range(1, t+1): # 1~216까지 반복
    a = list(map(int, str(i))) # 숫자인 것을 문자열해주고, 리스트에 넣기
    result = i + sum(a)# 자기 자신 그대로 + 각 자리수합
    if result == t: #result가 입력 받은 숫자와 같아야함
        print(i)
        break # for문 빠져나감
else:
    print(0)

