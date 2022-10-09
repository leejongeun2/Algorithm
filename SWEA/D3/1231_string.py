# 주어진 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램


for tc in range(10):
    N = int(input())
    target = input()
    sentence = input()
    result = sentence.count(target)
    print(f"#{N}, {result}") 
