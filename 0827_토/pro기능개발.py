# 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발 될 수 있음
# 이때, 뒤에 있는 기능은 앞에 있는 기능이 배포 될 때 함께 배포 됨

# progresses =  # 배포되어야 하는 순서대로 작업의 진도가 저힌 정수 배열
# speeds = # 각 작업의 개발 속도가 적힌 정수 배열

# 각 배포마다 몇 개의 기능이 배포되는지? 

pro = list(map(int, input().split()))
spe = list(map(int, input().split()))

