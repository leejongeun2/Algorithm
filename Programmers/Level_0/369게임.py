def solution(order):
    answer = 0
    for i in str(order): # 숫자를 문자열로 변경 "1234"
        if i in ["3", "6", "9"]:
            answer += 1
    return answer