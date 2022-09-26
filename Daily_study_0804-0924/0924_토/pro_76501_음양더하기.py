# 정수들의 절댓값을 차례대로 담은 정수배열과 이 정수들의 부호를 차례로 담은 배열이 있음
# 실제 정수들의 합을 구하는 프로그램

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        if b[i]:
            answer += a[i]
        else:
            answer -= a[i]
    return answer
        
