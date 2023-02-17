def solution(cipher, code):
    answer = ''
    for i in range(code, len(cipher)+1): # 리스트[시작인덱스:종료인덱스:인덱스증가폭]
        if i % code == 0:
            answer += cipher[i-1]
    return answer