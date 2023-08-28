class Cls:
    x = 10
    def add(self, a): # self는 객체 자체를 나타냄, 우리가 생성한 a(self는 이 클래스의 객체), a는 함수 호출할때 주어지는 값
        return a + self.x

a = Cls()
a.x = 5
print(a.add(5))

# self는 방금 만들어진 그 '쿠키'(객체) 자신을 가리키는 것입니다. 즉, 클래스 내에서 자기 자신을 참조할 때 사용하는 용어입니다.
# a = Cls()에서 a는 Cls 클래스를 기반으로 만들어진 객체입니다. 즉, '쿠키 틀'인 Cls로 만든 하나의 '쿠키'가 a입니다.