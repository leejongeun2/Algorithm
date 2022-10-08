# 치킨 시켜먹으면 한마리당 쿠폰 한장 발급
# 쿠폰 10장 모으면 치킨 한마리 서비스 , 서비스 치킨에도 쿠폰 발급 

chicken = 1081
answer = 0
while chicken >= 10: #10 미만이면 서비스치킨을 받을 수 없음

    coupon = chicken // 10
    na = chicken%10
    answer += coupon
    chicken = coupon + na

print(answer)