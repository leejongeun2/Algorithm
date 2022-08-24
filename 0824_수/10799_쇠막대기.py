# 쇠막대기를 아래에서 위로 겹쳐놓고, 레이저를 위에서 수직으로 발사하여 쇠막대기름 자름


n = list(input())
answer = 0
list1 = []

for i in range(len(n)):
    if n[i] == '(':
        list1.append('(')

    else:
        if n[i-1] == '(':
            list1.pop()
            answer += len(list1)

        else:
            list1.pop()
            answer += 1
            
print(answer)
