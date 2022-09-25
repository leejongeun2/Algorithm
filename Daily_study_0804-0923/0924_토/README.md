### pro_76501_음양더하기
* 리스트 길이가 같은 각 a, b  리스트끼리 인덱스값을 매칭하며 비교할 때, a의 길이로 for문을 잡고, 해당 i가 인덱스 값이니, if문에 해당 인덱스로 b를 인덱스 처리하고, a리스트를 조작함

    * answer = 0 
    ```for i in range(len(a))
    if b[i]: # b[i]가 참인 경우
    answer += b[i]
    else:
    answer -= a[i]
    ```