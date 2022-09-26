
# 외운 단어가 주어졌을 때 전화를 걸기 위한 시간
w = input()

dic = {"ABC":3, "DEF":4, "GHI":5, "JKL":6, "MNO":7, "PQRS":8, "TUV":9, "WXYZ":10}
# lis=[]
cnt = 0

for i in w:
    for j in dic.keys(): # w가 abc에 없다면, def도 확인
        if str(i) in j:
            cnt += dic[j]
print(cnt)
