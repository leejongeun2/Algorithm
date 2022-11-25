from collections import deque
# 큐를 구현하기 위해 deque 라이브러리 사용

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # 먼저들어온 것부터 삭제
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저들어온 순서대로 출력
queue.reverse() # 다음 출력
print(queue)
