# 입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자.단, 3항 연산을 사용한다.
a, b = input().split()
a = int(a)  #변수 a에 저장되어있는 값을 정수로 바꾸어 다시 변수 a에 저장
b = int(b)
c = (a if (a>=b) else b) # a가 b보다 크다면 a, 아니면 b => 3개의 요소로 이루어져서 3항 연산식이라고 부름
print(int(c))