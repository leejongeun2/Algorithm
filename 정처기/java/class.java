package 정처기.java;

class MethodEx { // { } 안에 멤버변수, 생성자 메소드 및 메소드 기술(클래스 정의)
int var1,var2;
public int sum(int a, int b){ 
return a+b;
}
public static void main(String[] args){
MethodEx me = new MethodEx(); // 클래스 이름 객체이름 = new 생성자메서드
int res = me.sum(1000, -10);
System.out.println("res="+res);
}
}