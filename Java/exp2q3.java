import java.util.*;

public class exp2q3 {
    public static void main(String args[]) {
        int arg[] = new int[10];
        arg[0] = Integer.parseInt(args[0]);
        arg[1] = Integer.parseInt(args[1]);
        arg[2] = Integer.parseInt(args[2]);
        arg[3] = Integer.parseInt(args[3]);
        arg[4] = Integer.parseInt(args[4]);
        arg[5] = Integer.parseInt(args[5]);
        arg[6] = Integer.parseInt(args[6]);
        arg[7] = Integer.parseInt(args[7]);
        arg[8] = Integer.parseInt(args[8]);
        arg[9] = Integer.parseInt(args[9]);
        for (int i = 0; i < 10; i++) {
            if (arg[i] < 40) {
                System.out.println("FAIL");
            } else if (arg[i] >= 40 && arg[i] < 51) {
                System.out.println("PASS");
            } else if (arg[i] > 50 && arg[i] < 76) {
                System.out.println("MERIT");
            } else {
                System.out.println("DISTINCTION");
            }
        }
    }
}
