# while문을 이용해 계속해서 반복하게 하려면, while문의 조건이 항상 참이 되도록 만들면 됨

# while 1:
#     print("find")
#     break

#======정상 출력===============

# num = 0
# while 1:
#     print(num)
#     if num == 10:
#         break
#     num += 1

#========5만 무한대로 나오는 출력..이 아니라 알고보니 0,1,2,3,4,55555=================


num = 0
while num < 10:
    print(num)
    if num == 5:
        continue
    num += 1
#
# continue 경우, 5가 무한대로 나오는 이유는? > 조건때문에 그런지? > 이유는 컨티뉴를 만나면 아래 코드는 실행되지 않기 떄문
# 정답 코드
# >>> num = 0
# >>> while num < 10:
#         num += 1
#         if num == 5:
#                 continue
#         print(num)
