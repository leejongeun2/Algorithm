# 문자열 s를 입력 받은 후에, 각 문자를 r번 반복해 새 문자열 p를 만든 후 출력하는 프로그램

t = int(input())

for i in range(t):
    r, s = input().split()
    for j in s:
        print(j*int(r),end="") # 공백 없이 옆으로 정렬 될 수 있도록
    print() # 엔드값을 입력하는 경우 다음 문자열도 줄넘김이 되지 않기 때문에 입력 받은 하나의 문자열이 출력되는 for 문이 끝나면 빈 프린트 함수로 인해 줄넘김이 되도록 함
   