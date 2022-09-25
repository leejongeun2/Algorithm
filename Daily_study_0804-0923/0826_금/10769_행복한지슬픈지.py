# 3개의 문자가 붙어있는 구조로 이루어진 이모티콘
# 행복한 얼굴을 나타내는 :-), 슬픈 얼굴을 나타내는 :-(가 있음
# 어떤 이모티콘도 포함되어있지 않으면 none을 출력
# 행복 이모티콘 = 슬픈 이모티콘의 수가 동일하게 포함되어있으면 unsure
# 행복 > 슬픈 happy
# 행복 < 슬픈 sad

import sys
sys.stdin = open("10769_input.txt")

Text = input()
happy = Text.count(':-)')
sad = Text.count(':-(')
if happy == 0 and sad == 0:
    print('none')
else:
    if happy > sad:
        print('happy')
    elif sad > happy:
        print('sad')
    else:
        print('unsure')