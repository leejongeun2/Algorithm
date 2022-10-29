w, h, b = map(int, input().split())

res = (w*h*b)/8/1024/1024


print('%.2f'%res,"MB") # round의 문제점은 숫자에 끝자리수가 0일때 원하는대로, 자릿수가 출력 안됨