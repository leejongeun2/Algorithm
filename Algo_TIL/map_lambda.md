## map 함수 적용\_*9/25 pro*가장큰수\_42746

### map이란?

- 리스트의 요소를 지정 된 함수로 처리해주는 함수
- map(int, input().split())
  - 입력 값을 숫자형으로 적용하는 것
- map(str, n)
  - n값을 문자 적용하는 것
  - 주의: list(str(n))하는 경우, 리스트의 괄호까지 모두 문자열로 리스트화 됨, 따라서 map을 사용하여 n의 요소만 문자열로 바꿔줌
* `n, m, k = map(int, input().split())` 띄어쓰기 기준으로 각 입력값을 숫자로 변경
* `data = list(map(int, input().split()))` # data처럼 하나의 변수로 배열을 입력 받을 때는 리스트화시켜줘야함(리스트를 안할 경우, 출력값이 객체로 표시됨)
* `plan = input().split()` 띄어쓰기 기준으로 문자를 입력 받을 때
* 참조: https://dojang.io/mod/page/view.php?id=2286

### lambda 사용법

- m.sort(key=lambda x: x\*3, reverse=True)
- lambda x: x\*3
  - m인자 각각의 문자열을 3번 반복한다는
    뜻 ex)6, 10, 2 => 666, 101010, 222
  - 문자열은 첫번째 인덱스 값으로 비교되어, 1<2<6이므로, 10<2<6 임
  - 여기서, 거꾸로 내림차순하면 6>2>10
