n, m = map(int, input().split())  # n개의 카드가 주어지고 기준이 되는 수 m을 입력받는다.
# 플레이어는 세 장의 카드를 골라 m을 넘지 않으면서 최대한 가까운 카드의 합을 완성해야한다.
# 완전탐색문제
arr = list(map(int, input().split()))
# 카드를 입력받는다.
result = 0

# 주어진 카드 갯수만큼 경우를 고려하여 반복을 돌린다. 이 때 세장을 선택하므로 하위 반복문도 세번 돌리도록 한다.
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i] + arr[j] + arr[k] > m:
                continue
            else:
                result = max(result, arr[i] + arr[j] + arr[k])

print(result)