import java.util.*;

public class exp3q1 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a three digits :");
        int i = sc.nextInt();
        int j = sc.nextInt();
        int k = sc.nextInt();
        for (int a = 0; a < 10; a++) {
            for (int b = 0; b < 10; b++) {
                for (int c = 0; c < 10; c++) {
                    if ((a == i || a == j || a == k) && (b == i || b == j || b == k) && (c == i || c == j || c == k)) {
                        System.out.print(a + " " + b + " " + c);
                    }
                    System.out.println();
                }
            }
        }
    }
}
