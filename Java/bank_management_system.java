import java.util.*;

class Admin {
    static int i = 0, k;
    static String name[] = new String[10];
    static int age[] = new int[10];
    static String acc_no[] = new String[10];
    static int contact_no[] = new int[10];
    static String password[] = new String[10];
    static float Deposit[] = new float[10];

    public static void create() {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter your name: ");
        name[i] = sc.next();
        System.out.println("Enter your age: ");
        age[i] = sc.nextInt();
        System.out.println("Enter your Account number given by manager: ");
        acc_no[i] = sc.next();
        System.out.println("Enter your contact info: ");
        contact_no[i] = sc.nextInt();
        System.out.println("Create a password: ");
        password[i] = sc.next();
        System.out.println("Enter amount of money you are depositing: ");
        Deposit[i] = sc.nextFloat();
        i = i + 1;
    }

    public static void update() {
        char resp;
        int flag = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your account number: ");
        String acc = sc.next();
        for (int j = 0; j < i; j++) {
            if (acc.equals(acc_no[j])) {
                flag++;
                k = j;
            }
        }
        if (flag == 0) {
            System.out.println("No account found: ");
        } else {
            System.out.println("Do you want to update your password press Y for yes and N for no:");
            resp = sc.next().charAt(0);
            if (resp == 'Y') {
                System.out.println("Enter new password: ");
                password[k] = sc.next();
            } else if (resp == 'N') {
                System.out.println("You are using your current password");
            } else {
                System.out.println("Invalid choice , Enter either Y or N ");
            }
            System.out.println("Do you want to update your contact number press Y for yes and N for no:");
            resp = sc.next().charAt(0);
            if (resp == 'Y') {
                System.out.println("Enter new contact number: ");
                contact_no[k] = sc.nextInt();
            } else if (resp == 'N') {
                System.out.println("Your are using your current contact info.");
            } else {
                System.out.println("Invalid choice , Enter either Y or N");
            }

        }
    }

    public static void deposit() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your account number: ");
        String acc = sc.next();
        for (int i = 0; i < 10; i++) {
            if (acc.equals(acc_no[i])) {
                System.out.println("Enter the amount you are depositing:");
                float deposit = sc.nextFloat();
                Deposit[i] = Deposit[i] + deposit;
                System.out.println(" Rs " + deposit + "Successfullly");
                System.out.println("You current balance is :" + Deposit[i]);
            } else {
                create();
            }
        }

    }

    public static void transaction() {
        Scanner sc = new Scanner(System.in);
        System.out.println(" Press 1 to withdraw money");
        int ch = sc.nextInt();
        if (ch == 1) {
            System.out.println("Enterr your atm number:");
            String acc = sc.next();
            for (int i = 0; i < 10; i++) {
                if (acc.equals(acc_no[i])) {
                    System.out.println("Enter your password:");
                    String pass = sc.next();
                    if (pass.equals(password[i])) {
                        System.out.println("Enter amount to be withdraw: ");
                        float withdraw = sc.nextFloat();
                        Deposit[i] = Deposit[i] - withdraw;
                    }
                }
            }
        }
    }
}

class bank_management_system extends Admin {

    public static void main(String args[]) {
        int flag = 0;
        Scanner sc = new Scanner(System.in);
        Admin ob = new Admin();
        System.out.println("Enter your atm number:");
        String acc = sc.next();
        for (int i = 0; i < 10; i++) {
            if ((acc).equals(acc_no[i])) {
                update();
                flag += 1;
            }
        }
        if (flag == 0) {
            create();
        }
    }
}