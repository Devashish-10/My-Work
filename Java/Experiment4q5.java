import java.util.*;

class Employee {
    protected String name;
    protected int empid;
    protected double salary;

    Employee(String name, int empid, double salary) {
        this.name = name;
        this.empid = empid;
        this.salary = salary;
    }

    String namedisplay() {
        return name;
    }

    double salarydisplay() {
        return salary;
    }

    double increasesalary(float perc) {
        salary += salary * perc / 100;
        return salary;
    }
}

class Manager extends Employee {
    Manager(String name, int empid, double salary) {
        super(name, empid, salary);
    }

    void details() {
        String n = super.namedisplay();
        double sal = super.salarydisplay();
        System.out.println(n);
        System.out.println(sal);
    }

    void salinc(float perc) {
        double sal = super.increasesalary(perc);
        System.out.println("New Salary :" + sal);
    }
}

class Experiment4q5 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        Manager department = new Manager("Ajay", 123, 50000.0);
        department.details();
        System.out.println("Enter hike in salary :");
        float hike = sc.nextFloat();
        department.salinc(hike);
    }
}