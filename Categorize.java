import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        if(h<150)
        {
            System.out.println("Person is Dwarf");
        }
        else if(h>150 && h<=165)
        {
            System.out.println("Person is average heighted");
        }
        else if(h>165 && h<=195)
        {
            System.out.println("Person is taller");
        }
        else{
            System.out.println("Abnormal height");
        }
    }
}
