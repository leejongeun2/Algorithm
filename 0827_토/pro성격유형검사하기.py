# sorted


# survey = ["RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"] # 질문마다 판단하는 지표를 담은 리스트
# choices = [] # 검사자가 각 질문마다 선택한 선택지를 담은 리스트
score = {"A":0, "N":0, "C":0, "F":0, "M":0, "J":0, "R":0, "T":0}
# surveyli = []
answer = ''
survey1 = input().split()
choices1 = list(map(int, input().split()))

# 입력 받은 문제 유형 리스트(surbey1)와 선택지 담은 리스트(choices1)를 비교하고 
# 그 안에서 앞의 알파벳, 뒤의 알파벳 별 점수 조건?을 넣어 줘야 할 것 같음...  
for i in range(len(survey1)):
    l = survey1[i][0] #a #c => 문자열인데, 인덱싱 할 수 있구낭..
    r = survey1[i][1] #n #f
    if choices1[i] -4 > 0: #1 # 왜 -4를 하는지? => 모르겠음과의 차이가 나올 수 있도록!
        score[r] += choices1[i]-4 # 0 += 5-4 => a:1
    elif choices1[i]-4 < 0: # 3-4
        score[l] += 4-choices1[i] # f:1(4-3)

answer += "R" if score["R"] >= score["T"] else "T"
answer += "C" if score["C"] >= score["F"] else "F"
answer += "J" if score["J"] >= score["M"] else "M"
answer += "A" if score["A"] >= score["N"] else "N"

print(answer)
