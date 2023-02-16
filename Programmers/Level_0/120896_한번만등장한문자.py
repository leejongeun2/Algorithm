def solution(s):
    answer = ''
    for i in s:
        if s.count(i) == 1: 
            answer += i
    return ''.join(sorted(answer)) # str형식에서는 sort()를 사용하지못하기에, sorted(answer)를 통해서 원본 리스트나 str를 변경하지하고 정렬해준다.
    # sorted 한 값은 리스트다. ['a', 'd', 'e', 'f'] 이것을 문자열로 자연스럽게 이어주기 위해서 공백을 join을 사용해준다.