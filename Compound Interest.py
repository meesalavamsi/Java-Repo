import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        double P = sc.nextDouble();
        double R = sc.nextDouble();
        int T = sc.nextInt();
        double A = P*Math.pow(1+(R/100),T);
        double ci = A-P;
        System.out.println(String.format("%.2f",ci));
    }
}