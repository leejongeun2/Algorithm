# 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발 될 수 있음
# 이때, 뒤에 있는 기능은 앞에 있는 기능이 배포 될 때 함께 배포 됨

# progresses =  # 배포되어야 하는 순서대로 작업의 진도가 저힌 정수 배열
# speeds = # 각 작업의 개발 속도가 적힌 정수 배열

# 각 배포마다 몇 개의 기능이 배포되는지? 

# pro = list(map(int, input().split()))
# spe = list(map(int, input().split()))

pro = [93, 30, 55]
spe = [1, 30, 5]

result = []    
cnt = 0

while pro: 
    if pro[0] >= 100:
        pro.pop(0)
        spe.pop(0)
        cnt += 1
    else:
        result.append(cnt)
        cnt = 0
        for i in range(len(pro)):
            pro[i] += spe[i]
result.append(cnt)
qw = []
for i in range(len(result)):
    if result[i] != 0:
        qw.append(result[i])
print(qw)



