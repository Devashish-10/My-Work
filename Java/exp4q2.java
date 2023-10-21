public class Player {

    void details(String name, String sports, int age) {
        System.out.println("Player name:" + name);
        System.out.println("Player sports:" + sports);
        System.out.println("Player age:" + age);
    }
}

public class Cricket_player extends Player {
    void printdetails() {
        Player obj = new Player();
        obj.details("Virat", "Cricket", 34);
    }
}

public class Football_player extends Player {
    void printdetails() {
        Player obj = new Player();
        obj.details("Messi", "Football", 35);
    }
}

public class Hockey_player extends Player {
    void pintdetails() {
        Player obj = new Player();
        obj.details("Dhyanchand", "Hockey", 34);
    }
}

public class exp4q2 extends Cricket_player,Hockey_player,Football_player{

    public static void main(String args[]) {
        Cricket_player obj1 = new Cricket_player();
        Football_player obj2 = new Football_player();
        Hockey_player obj3 = new Hockey_player();
        obj1.printdetails();
        obj2.printdetails();
        obj3.pintdetails();
    }
}
