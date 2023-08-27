public class P242 {

    public static void main(String[] args) {

    }

    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;

        int[] s_characters = new int[26];
        int[] t_characters = new int[26];
        for (int i = 0; i < s.length(); i++) {
            s_characters[((int) s.charAt(i)) - 97]++;
            t_characters[((int) t.charAt(i)) - 97]++;
        }
        for (int i = 0; i < s_characters.length; i++) {
            if (s_characters[i] != t_characters[i])
                return false;
        }
        return true;
    }
}

// Given two strings s and t, return true if t is an anagram of s, and false
// otherwise.

/*
 * questions i would ask:
 * are two strings an anagram of one another if one uses the same letters
 * multiple times?
 */