# 서로 다른 7개의 정수 중에서 3개의 정수를 골라 합을 구해서 수를 만듬
# 이렇게 만들 수 있는 수중에서 5번째로 큰 수를 출력하는 프로그램

# itertools.combinations(iterable, r)은 반복 가능 객체 중에서 r개를 선택한 조합을 이터레이터로 반환하는 함수

from itertools import combinations

t = int(input())
for tc in range(1, t + 1) :
    data = list(map(int, input().split()))
    result = []
    for value in combinations(data, 3) :
        result.append(sum(value))

    result = list(set(result))
    result.sort(reverse=True)
    print('#%d %d' % (tc, result[4]))