# 9550 9556 9550 9553 9558 9551 9551 9551

# 9556 9550 9553 9558 9551 9551 9551 9549

import sys

sys.stdin = open("input (6).txt")


t = 10
for t in range(1, t+1):
    tc = int(input())
    queue = list(map(int, input().split()))

    i = 1
    while True:
        if i > 5: # 5 감소 후 뒤로 이동한 것이 1개의 싸이클이므로, 다시 1 감소 후로 진행되어야 하기 때문에
            i = 1 # 다시 1 감소하는 싸이클로 가기 위해 위의 경우 i를 1로 셋팅
        t = queue.pop(0) - i # queue리스트에서 맨 앞 값을 추출-1하여 t로 지정
        if t <= 0 : # 0보다 작아지거나 0일 경우, 0으로 으로 저장 되며, 해당 숫자배열이 암호가 된다는 것이 문제에서 주어짐
            queue.append(0) 
            break
        queue.append(t) # 뒤에 추가 됨
        i += 1 # i 숫자가 1 씩 증가 

    
    print(f'#{tc}', *queue)