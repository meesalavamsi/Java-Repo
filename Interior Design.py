import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int x1 = sc.nextInt();
        int y1 = sc.nextInt();
        int x2 = sc.nextInt();
        int y2 = sc.nextInt();
        int cost1 = x1+y1;
        int cost2 = x2+y2;
        int total = Math.min(cost1,cost2);
        System.out.println(total);
    }
}