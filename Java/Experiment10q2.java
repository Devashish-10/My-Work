import java.util.*;

public class Experiment10q2 {
    public static void main(String args[]) {
        int c1 = 0, c2 = 0;
        Scanner sc = new Scanner(System.in);
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        map.put(1, 1);
        map.put(2, 4);
        map.put(3, 9);
        map.put(4, 16);
        for (Map.Entry m : map.entrySet()) {
            System.out.println("Key:" + m.getKey());
            System.out.println("Value:" + m.getValue());
        }
        System.out.println("Enter the key you want to check: ");
        int k = sc.nextInt();
        System.out.println("Enter a value to want to check: ");
        int v = sc.nextInt();
        for (Map.Entry m : map.entrySet()) {
            if (m.getKey().equals(k)) {
                c1 += 1;
            }
            if (m.getValue().equals(v)) {
                c2 += 1;
            }
        }
        if (c1 > 0) {
            System.out.println("It has the entered key");
        } else {
            System.out.println("It does not have the entered key");
        }
        if (c2 > 0) {
            System.out.println("It has entered value");
        } else {
            System.out.println("It does not havew the enetered value");
        }

    }
}
