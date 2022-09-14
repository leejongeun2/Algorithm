t = int(input())

n = int(input())

dic = {}

for i in range(t):
    m = map(int, input().split())

    if m 
    
    


t = int(input())

for _ in range(t) :
    tc = int(input())
    score = list(map(int, input().split()))
    data = [0] * 1001

    for i in score :
        data[i] += 1

    max_value = max(data)
    result = []
    for i in range(len(data)) :
        if data[i] == max_value :
            result.append(i)

    print('#%d %d' % (tc, max(result)))