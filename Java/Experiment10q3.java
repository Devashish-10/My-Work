import java.util.*;

class Experiment10q3 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        HashSet<String> set = new HashSet<String>();
        set.add("Asus");
        set.add("Dell");
        set.add("HP");
        set.add("Acer");
        Iterator<String> itr = set.iterator();
        System.out.println("Enter what you want to find:");
        String s = sc.next();
        int c = 0;
        while (itr.hasNext()) {
            if (itr.next().equals(s)) {
                c += 1;
            }
        }
        if (c > 0) {
            System.out.println(("Entered object present inn the list:"));
        } else {
            System.out.println(("Entered object not present inn the list:"));
        }
        set.clear();
        System.out.println("All elements deleted");
        System.out.println(set);
    }
}
