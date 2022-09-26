# table = []

# n, m = list(map(int, input().split()))

# table.append(n)

# print(table)

table = []
# 1 2
for _ in range(3):
    n, m = list(map(int, input().split())) # [1, 2]=> 언패킹 되면서 n = 1 m = 2
    # data = list(map(int, input().split())) 
    table.append(n) # n을 어펜딩할 때, [4, 2, 3]
   

print(table) # [[4, 6], [2, 5], [3, 4]]

