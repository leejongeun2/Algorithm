## 알게 된 것
---

### swea_모음이 보이지 않는 사람_4406
1. 문자열도 인덱스 탐색이 가능함
2. replace는 문자열에만 가능
3. end는 한줄씩 출력했고 한줄 띄어서 출력 된 것도 모아서 하나의 줄로 출력 가능하게 만듬
4. 리스트 공백은 별표를 하든 for문을 돌리든 공백은 나옴
5. not in은 리스트에 포함되지 않는 것들 출력
6. 리스트 아니어도 문자열을 빈 변수에 할당해서 +=를 사용해서 출력 할 수 있음

### 파일경로
* cd 는 디렉토리 변경의 줄임말
1. ./ 경우 상위폴더에서 > 하위폴더로 이동할 때
2. ../ 경우 동일한(형제)상의 폴더로 이동할 때, 한번 상위로 올라갔다가 가야 되기 때문
3. 현재 있는 폴더에서 한단계 상위 폴더로 이동함

### 2941_크로아티아
* replace 경우, 문자열 원형 자체를 변형시키지 않기 떄문에, 새로운 변수명으로 할당 시, 원래문자열 기준으로 대체됨
=> 따라서 동일한 변수명으로 지정하여 벼경 된 값이 저장 될 수 있도록 해야함.

### 1357_뒤집힌덧셈
```
s = 'abcde'
s_reverse = ''  # 기존 문자열을 역순으로 담아줄 빈 문자열 선언
for char in s:
    s_reverse = char + s_reverse

print(s_reverse)  # edcba
```

```
s = 'abcde'
print(''.join(reversed(s)))  # 'edcba'
reversed는 reverse와는 달리 문자열에도 바로 적용이 가능하며 반복자 변환값이 생기기 때문에 조인을 붙여줘야함, (reverse는 list에만 사용 가능, 변환값 없이 자기자신을 변경)

```
```
string = 'Hello, World!'
reversed_str = ''
for i in string:
    reversed_str = i + reversed_str

print(f'Original String: {string}')
print(f'Reversed String: {reversed_str}')
```
```
# x1 = int(str(x)[::-1])
# y1 = int(str(y)[::-1])
# sum1 = x1+y1
# sum2 = int(str(sum1)[::-1])
# print(sum2)
```