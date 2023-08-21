public class P1893 {
    public static void main(String[] args) {

        int[][] range = { { 1, 2 }, { 4, 6 }, { 20, 50 } };
        System.out.println(isCovered(range, 3, 3));
    }

    /*
     * create an array of booleans, size 50, all set to false
     * iterate through the array of ranges, using the ranges given, iterate through
     * the boolean array and set the respective indices to true if they are included
     * in the range
     */

    public static boolean isCovered(int[][] ranges, int left, int right) {
        boolean[] covered = new boolean[50];
        for (int i = 0; i < ranges.length; i++)
            for (int m = ranges[i][0] - 1; m <= ranges[i][1] - 1; m++)
                covered[m] = true;
        for (int i = left - 1; i <= right - 1; i++) {
            if (!covered[i])
                return false;
        }

        return true;
    }
}
