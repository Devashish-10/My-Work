public class exp3q4 {
    public static void main(String args[]) {
        int sum = 0;
        for (int i = 41; i < 250; i++) {
            if (i % 5 == 0) {
                System.out.println(i);
                sum += i;
                System.out.println(sum);
            }
        }
    }
}
