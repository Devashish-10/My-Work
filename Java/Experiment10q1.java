import java.util.*;

public class Experiment10q1 {
    public static void main(String args[]) {
        ArrayList<String> list = new ArrayList<String>();
        list.add("Hello");
        list.add("Hi");
        list.add("Bye");
        Iterator itr = list.iterator();
        while (itr.hasNext()) {
            System.out.println(itr.next());
        }
        ArrayList<String> arraylistclone = (ArrayList<String>) list.clone();
        System.out.println(arraylistclone);
        for (int i = list.size() - 1; i >= 0; i--) {
            String element = list.get(i);
            System.out.print(element + " ");
        }
    }
}
