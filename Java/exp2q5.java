import java.util.*;

public class exp2q5 {
    public static void main(String args[]) {
        int no_of_rows = Integer.parseInt(args[0]);
        for (int i = 0; i < no_of_rows; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
