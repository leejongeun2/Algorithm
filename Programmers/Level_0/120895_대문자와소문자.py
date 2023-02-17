def solution(my_string):
    answer = ''
    my_string = list(my_string)
    for i in my_string:
        if i.isupper(): # 만약 isupper()를 이용하여 대문자인지 판단한 결과가 True이면 대문자이기 때문에 lower()를 사용해 소문자로 바꿔주고 answer에 붙인다.
            answer += i.lower()
        else:
            answer += i.upper()
    return answer