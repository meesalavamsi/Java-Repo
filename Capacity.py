import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int S = sc.nextInt();
        int B = sc.nextInt();
        int C = T*S*B*1;
        System.out.println(C +" KB ");
    }
}