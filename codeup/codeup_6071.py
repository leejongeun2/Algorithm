# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.


n = 1      #처음 조건 검사를 통과하기 위해 0 아닌 값을 임의로 저장
while n!=0 :
  n = int(input())
  if n!=0 : 
    print(n)



# 이렇게 간다면 0도 출력 됨, 왜냐! 이전 인풋 값으로 while조건식이 나오 실행되기 때문! 
# 그래서 if문을 while문안에 넣어줘야함
# while문 바깥에 input을 넣으면 한번밖에 입력 안됨요
n = 1 
while n!=0 :
  n = int(input()) 
  print(n)