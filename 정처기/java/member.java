package 정처기.java;

class Gogaek{
String irum; // 멤버 변수 선언
int nai;
long bunho;
static long GoBunho=0;
public Gogaek(){
bunho = GoBunho++;
}
}

class VarDemo{
public static void main(String args[]){
Gogaek gogaek1=new Gogaek();
Gogaek gogaek2=new Gogaek();
Gogaek gogaek3=new Gogaek();

gogaek1.irum = "컴퓨터";
System.out.println("고객1 이름 : "+gogaek1.irum);
System.out.println("gogaek1의 id의 번호:"+ gogaek1.bunho);
System.out.println("gogaek2의 id의 번호:"+ gogaek2.bunho);
System.out.println("gogaek3의 id의 번호:"+ gogaek3.bunho);
System.out.println("전체 고객 수 : "+Gogaek.GoBunho+"명");
}
}