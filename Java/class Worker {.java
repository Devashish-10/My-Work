class Worker {
    protected double rate;

    void details(String name, double rate) {

        System.out.println("Worker Nam " + name);
        System.out.println("Worker Rate per hour of work: " + rate);
    }

    double Compay(int hours) {
        double pay = hours * rate;
        return pay;
    }
}

class Dailyworker extends Worker {
    void detailsprint() {
        Worker ob = new Worker();
        ob.details("Ajay", 850.0);
        double sal = ob.Compay(8 * 7);
        System.out.println(sal);
    }
}

class SalariedWorker extends Worker {
    void detailsprint() {
        Worker ob = new Worker();
        ob.details("Ajay", 1050.0);
        double sal = ob.Compay(40);
        System.out.println(sal);
    }
}

class exp4q3 {

    public static void main(String args[]) {
        Dailyworker ob1 = new Dailyworker();
        SalariedWorker ob2 = new SalariedWorker();
        ob1.detailsprint();
        ob2.detailsprint();
    }
}
