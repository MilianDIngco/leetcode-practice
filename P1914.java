public class P1914 {
    public static void main(String[] args) {
        int a = 4, b = 4;
        int[][] arr = new int[a][b];
        for (int i = 0; i < a; i++)
            for (int n = 0; n < b; n++)
                arr[i][n] = 0;
        for (int i = 0; i < ((a < b) ? (a / 2) : (b / 2)); i++)
            arr[i][i] = 1;
        printArr(arr);
        System.out.println();
        // int[][] arrCpy = new int[a][b];
        long c = 5284823040L;
        rotateGrid(arr, c);
        printArr(arr);
    }

    public static void copyArr(int[][] arr, int[][] arrCpy, int a, int b) {
        for (int i = 0; i < a; i++)
            for (int n = 0; n < b; n++)
                arrCpy[i][n] = arr[i][n];
    }

    public static void printArr(int[][] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int n = 0; n < arr[i].length; n++) {
                System.out.print(arr[i][n] + " ");
            }
            System.out.println();
        }
    }

    public static void cycle(int[][] arr, int left, int right, int top, int bot) {
        int x = left, y = top + 1;
        int xPrev = x, yPrev = y - 1;
        while (y < bot) {
            swap(arr, yPrev, xPrev, y, x);
            y++;
        }
        while (x < right) {
            swap(arr, yPrev, xPrev, y, x);
            x++;
        }
        while (y > top) {
            swap(arr, yPrev, xPrev, y, x);
            y--;
        }
        while (x >= left) {
            swap(arr, yPrev, xPrev, y, x);
            x--;
        }
    }

    public static void swap(int[][] arr, int y1, int x1, int y2, int x2) {
        int temp = arr[y2][x2];
        arr[y2][x2] = arr[y1][x1];
        arr[y1][x1] = temp;
    }

    public static int[][] rotateGrid(int[][] grid, long k) {
        int right = (grid.length < grid[0].length) ? grid[0].length - (grid.length / 2 - 1) - 1
                : grid[0].length / 2;
        int left = (grid.length < grid[0].length) ? grid[0].length - right - 1 : right - 1;
        int top = left;
        int bot = (grid.length < grid[0].length) ? top + 1 : grid.length - top - 1;
        for (int i = 0; i < ((grid.length < grid[0].length) ? grid.length / 2 : grid[0].length / 2); i++) {
            System.out.println(left + " " + right + " " + top + " " + bot);
            for (int n = 0; n < (k % ((right - left + 1) * 2 + (bot - top + 1) * 2 - 4)); n++) {
                cycle(grid, left, right, top, bot);
            }
            left--;
            right++;
            top--;
            bot++;
        }
        return grid;
    }
}

/*
 * what i know:
 * always rotates counterclockwise
 * m and n are always even
 * 
 * what i can deduce:
 * since they are always even, when i divide n by 2, i can get the very smallest
 * cycle's rightmost edge. n/2 - 1 gets the smallest leftmost edge.
 * (n/2+1) is the smallest topmost edge
 * m-(n/2+1) is the smallest bottommost edge
 * 
 * what my plan is:
 * I intend to make a for loop that runs n/2 times (because the amount of cycles
 * are half the width of the rectangle)
 * I'll have two integer variables keeping track of the indices that will be
 * used to cycle through and point to the next square to replace
 * 
 * for(int i = 0; i < 4; i++) {
 * for(int n = start; n < end; n++) {
 * 
 * }
 * change start and end to the next
 * }
 * 
 * clarifying questions i would ask:
 * 
 */

// for (int i = 0; i < k; i++) {
// int right = (grid.length < grid[0].length) ? grid[0].length - (grid.length /
// 2 - 1) - 1
// : grid[0].length / 2;
// int left = (grid.length < grid[0].length) ? grid[0].length - right - 1 :
// right - 1;
// int top = left;
// int bot = (grid.length < grid[0].length) ? top + 1 : grid.length - top - 1;
// for (int n = 0; n < numCycles; n++) {
// cycle(grid, left--, right++, top--, bot++);
// }
// numRan++;
// }