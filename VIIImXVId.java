/**
 * VIIImXVId
 */
public class VIIImXVId {

    public static void main(String[] args) {
        System.out.println(equalFrequency("abbcc"));
    }

    public static boolean equalFrequency(String word) {
        // find the frequency of each letter
        int minFreq = 999999, maxFreq = -1, sumDiff = 0;
        int freq[] = new int[26];
        for (int i = 0; i < word.length(); i++)
            freq[((int) word.charAt(i)) - 97]++;
        for (int i = 0; i < word.length(); i++) {
            int charIndex = ((int) word.charAt(i)) - 97;
            minFreq = (freq[charIndex] < minFreq) ? freq[charIndex] : minFreq;
            maxFreq = (freq[charIndex] > maxFreq) ? freq[charIndex] : maxFreq;
        }
        for (int i = 0; i < freq.length; i++) {

        }
        if (minFreq == maxFreq && maxFreq == 1)
            return true;

        // false when sum is > 1, sum == 0,
        return (sumDiff == 1);
    }

}