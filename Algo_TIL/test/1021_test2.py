# 사람의 이름을 기분으로 주어진 문자열을 익명화 하는 함수 작성

# anonymize_text('John is old') == 'XXXX is old'
# anonymize_text('Mark Oldham ate an apple') == 'XXXXXXXXXXX ate an apple'

import spacy

nlp = spacy.load("en_core_web_sm")

print(nlp)
