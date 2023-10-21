import java.util.*;

interface Square {
    public void sq(int n);
}

class Arithematic implements Square {
    public void sq(int n) {
        int Square = n * n;
        System.out.println("The square is :" + Square);
    }
}

class Experiment5q1 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int n = sc.nextInt();
        Arithematic ob = new Arithematic();
        ob.sq(n);

    }
}