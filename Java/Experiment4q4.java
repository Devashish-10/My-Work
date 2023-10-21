import java.util.Scanner;

abstract class TrunkCall {
    protected int duration;

    public TrunkCall(int duration) {
        this.duration = duration;
    }

    public abstract double calculateCharges();
}

class OrdinaryTrunkCall extends TrunkCall {
    public OrdinaryTrunkCall(int duration) {
        super(duration);
    }

    public double calculateCharges() {
        return duration * 1.0;
    }
}

class UrgentTrunkCall extends TrunkCall {
    public UrgentTrunkCall(int duration) {
        super(duration);
    }

    public double calculateCharges() {
        return duration * 2.0;
    }
}

class LightningTrunkCall extends TrunkCall {
    public LightningTrunkCall(int duration) {
        super(duration);
    }

    public double calculateCharges() {
        return duration * 3.0;
    }
}

public class Experiment4q4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the duration of the trunk call (in minutes): ");
        int duration = scanner.nextInt();

        System.out.println("Select the type of trunk call:");
        System.out.println("1. Ordinary");
        System.out.println("2. Urgent");
        System.out.println("3. Lightning");
        System.out.print("Enter your choice: ");
        int choice = scanner.nextInt();

        TrunkCall call;

        switch (choice) {
            case 1:
                call = new OrdinaryTrunkCall(duration);
                break;
            case 2:
                call = new UrgentTrunkCall(duration);
                break;
            case 3:
                call = new LightningTrunkCall(duration);
                break;
            default:
                System.out.println("Invalid choice. Exiting program.");
                return;
        }

        double charges = call.calculateCharges();
        System.out.println("Charges for the trunk call: $" + charges);

        scanner.close();
    }
}
