public class P2506 {
    public static void main(String[] args) {

    }

    public static int similarPairs(String[] words) {
        boolean letters[][] = new boolean[words.length][26];
        // This array will be used to keep track of which boolean arrays have already
        // been counted
        int arrays[] = new int[26];
        for (int i = 0; i < arrays.length; i++)
            arrays[i] = i;

        // This will set each boolean array equal to the letters each word contains
        int numPairs = 0;
        for (int i = 0; i < words.length; i++)
            for (int n = 0; n < words[i].length(); n++)
                letters[i][(int) words[i].charAt(n) - 97] = true;

        // This will iterate through each boolean array and see if it matches. if it
        // does,
        for (int i = 0; i < letters.length - 1; i++) {
            for (int n = i + 1; n < letters.length; n++) {
                if (compareArray(letters[i], letters[n]))
                    numPairs++;
            }
        }
        return numPairs;
    }

    public static boolean compareArray(boolean[] aOne, boolean[] aTwo) {
        for (int i = 0; i < aOne.length; i++) {
            if (aOne[i] != aTwo[i])
                return false;
        }
        return true;
    }

    /*
     * subsets!!!
     * 
     * idea numero uno
     * create an array of strings
     * for each string in words
     * 
     * 12345
     * 12 13 14 15 23 24 25 34 35 45
     * 
     */
}
