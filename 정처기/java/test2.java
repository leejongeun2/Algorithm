package 정처기.java;

public class test2 {
    public static void main(String[] args) {
        int i =0;
        int sum=0;

        while(i<5) {
            i++;
            if (i%2 == 1)
            continue;
            sum +=i;
        }
        System.out.println(sum);
    }
}
