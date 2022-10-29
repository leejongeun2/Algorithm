# 1, 2, 3 ... 을 계속 더해 나갈 때,
# 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
# 계속 더하는 프로그램을 작성해보자.

n = int(input())
a = 0 # 합
t = 0

while a<n : 
    t = t+1
    a = a+t
print(t) # 마지막에 더한 정수 출력

#----
count = 0
for i in range(50): # 50정도 되야, 합이 1000이 넘음(문제에서는 1000까지로 합을 제한)
    count = count + i
print(count)