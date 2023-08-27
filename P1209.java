import java.util.Stack;

public class P1209 {
    public class Dupe {
        int numOccurances = 0;
        char character;

        Dupe(int numOccurances, char character) {
            this.numOccurances = numOccurances;
            this.character = character;
        }

        Dupe(char character) {
            this(1, character);
        }

        public void incOccurances(int a) {
            numOccurances += a;
        }

        public int getNumOccurances() {
            return numOccurances;
        }

        public char getCharacter() {
            return character;
        }
    }

    public static void main(String[] args) {
        P1209 a = new P1209();
        a.removeDupe("ccaaac", 3);
    }

    public String removeDupe(String str, int k) {
        if (str.length() < k)
            return str;

        Stack<Dupe> dupeStack = new Stack<Dupe>();
        char prev = str.charAt(0), curr;
        dupeStack.push(new Dupe(prev));
        for (int i = 1; i < str.length(); i++) {
            curr = str.charAt(i);
            if (curr == prev && !dupeStack.empty())
                ((Dupe) dupeStack.peek()).incOccurances(1);
            else
                dupeStack.push(new Dupe(curr));

            if (!dupeStack.empty() && ((Dupe) dupeStack.peek()).getNumOccurances() >= k) {
                System.out.print(((Dupe) dupeStack.peek()).numOccurances);
                System.out.println(((Dupe) dupeStack.pop()).character);
            }
            prev = (!dupeStack.empty()) ? (((Dupe) dupeStack.peek()).getCharacter()) : curr;
        }
        while (!dupeStack.empty()) {
            System.out.print(((Dupe) dupeStack.pop()).getCharacter());
        }

        return str;
    }

}
