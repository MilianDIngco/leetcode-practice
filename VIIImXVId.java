/**
 * VIIImXVId
 */
public class VIIImXVId {

    public static void main(String[] args) {
        System.out.println(equalFrequency("aaaaabb"));
    }

    public static boolean equalFrequency(String word) {
        // find the frequency of each letter
        int numOnes = 0;
        int sum = 0, n = 0, min = 200, max = 0;
        int freq[] = new int[26];
        for (int i = 0; i < word.length(); i++) {
            freq[((int) word.charAt(i)) - 97]++;
        }
        for (int i = 0; i < freq.length; i++) {
            numOnes += (freq[i] == 1) ? 1 : 0;
            if (freq[i] != 0) {
                sum += freq[i];
                n++;
                min = (freq[i] < min) ? freq[i] : min;
                max = (freq[i] > max) ? freq[i] : max;
            }
        }
        if (max - min > 1 && numOnes < 1)
            return false;
        if (numOnes == 1 || sum == n)
            return (sum - 1) % (n - 1) == 0;
        else
            return (sum - 1) % n == 0;
    }
}
