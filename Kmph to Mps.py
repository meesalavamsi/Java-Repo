import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int kmph = sc.nextInt();
        double mps = kmph/3.6;
        System.out.println(String.format("%.2f",mps));
    }
}