import java.util.Scanner;
public class Main{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int height = sc.nextInt();
        double centimeters = height*2.54;
        System.out.println(String.format("%.2f",centimeters));
    }
}