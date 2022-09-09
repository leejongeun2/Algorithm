# 회문: 거꾸로 읽어도 제대로 읽은 것과 같은 문장
# 회문이면 1 출력, 아니면 0 출력

t = int(input())

for _ in range(1, t+1):

    w = input()
    wr= str(''.join(reversed(w)))

    # print(''.join(wr))

    if w == wr:
        print(f'#{_} 1')
    else:
        print(f'#{_} 0')


# w = input()
# wr = input()

# if w == wr:
#     print(1)
# else:
#     print(0)
