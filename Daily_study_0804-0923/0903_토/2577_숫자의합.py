# 3개의 자연수 a,b,c가 주어질 때, a*b*c를 계산한 결과에 0부터 
#9까지 각각의 숫자가 몇번 쓰였는지 구하시오.




a = int(input())
b = int(input())
c = int(input())

result = list(str(a*b*c))

# print(result)

for i in range(10):
    m = result.count(str(i))
    print(m, type(m))
    





    
