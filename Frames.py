import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int X = sc.nextInt();
        int perimeter = 2*(N+M);
        int cost = perimeter*X;
        System.out.println(cost);
    }
}