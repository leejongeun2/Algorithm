# 클래스 없이 메소드만 단독 사용하는 경우

def calc(x, y):
    x *= y
    return x

a, b = 3, 4
a = calc(a, b) 
print(a, b) # x의 값 12를 a에 저장한 후 a값 출력