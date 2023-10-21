public class exp4q1 {
    private void print() {
        System.out.println("Hello World");
    }
}

public class subclass extends exp4q1 {
    public static void main(String args[]) {
        exp4q1 obj = new exp4q1();
        obj.print();
    }
}
