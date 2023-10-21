class Worker {
    protected String name;
    protected double rate;

    Worker(String name, double rate) {
        this.name = name;
        this.rate = rate;
    }

    void details() {

        System.out.println("Worker Nam " + name);
        System.out.println("Worker Rate per hour of work: " + rate);
    }

    double Compay(int hours) {
        double pay = hours * rate;
        return pay;
    }
}

class Dailyworker extends Worker {
    Dailyworker(String name, double rate) {
        super(name, rate);
    }

    void detailprint() {
        details();
        double sal = Compay(8 * 7);
        System.out.println(sal);
    }
}

class SalariedWorker extends Worker {
    SalariedWorker(String name, double rate) {
        super(name, rate);
    }

    void detailprint() {
        details();
        double sal = Compay(40);
        System.out.println(sal);
    }
}

class Experiment4q3 {

    public static void main(String args[]) {
        Dailyworker ob1 = new Dailyworker("Arun", 850);
        SalariedWorker ob2 = new SalariedWorker("Ajay", 1050);
        ob1.detailprint();
        ob2.detailprint();
    }
}
