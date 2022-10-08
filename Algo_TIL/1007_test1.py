# 켈리는 샘이 처음에 앞서 있기 때문에 더 많이 연습
# 샘 > 켈리
# 켈리가 샘보다 더 많은 문제를 푸는데 필요한 최소 일수
# 
import sys


sd = int(sys.stdin.readline()) # 4
kd = int(sys.stdin.readline()) # 5
de = int(sys.stdin.readline()) # 1

ss = de + sd # 4+1=5
ks = kd # 5

result = 1
if sd == kd:
    print(-1)
else:
    while ss > ks or ss == ks: 
        ss += sd # 5+4
        ks += kd # 5+5
        result += 1 
    print(result)
    


