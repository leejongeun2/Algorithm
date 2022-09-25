# 각 반의 학생들의 수학 성적이 주어지고 최대점수, 최수, 점수 차이를 구하는 프로그램을 작성
# 첫쨰 줄에 중덕 고등학교에 있는 반의 수
# 다음 줄에는 각 반의 학생수 n과 각 학생의 수학 성적이 주어짐

while True:
    n = int(input())
    if n == 0:
        break
    else:
        lis = []
        for _ in range(n):
            word = input()
            lis.append(word)
        lis.sort(key=str.lower)
        
        print(lis[0])