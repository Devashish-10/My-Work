import java.util.*;

public class exp3q2 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int a[] = new int[100];
        int sum = 0;
        System.out.println("Enter size of array:");
        int n = sc.nextInt();
        System.out.println("Enter array elements:");
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            a[i] = a[i] * a[i];
            sum += a[i];
        }
        System.out.println(sum);
    }
}
