import java.util.List;

/**
 * Leetcod
 */
public class Leetcod {

    public static void main(String[] args) {
        char abc = 65;
        System.out.println(abc);
        for (int i = 0; i < 26; i++) {
            for (int n = 1; n < 19; n++) {
                System.out.print(abc + "" + n + ", ");
            }
            System.out.println();
            abc++;
        }
    }

    public static int roadsAndLibraries(int n, int c_lib, int c_road, int cities_rows, int cities_columns,
            int cities[][]) {
        if (c_lib <= c_road)
            return c_lib * n;

        // run union find
        int[] size = new int[n + 1];
        size[0] = 0;
        for (int i = 1; i < n + 1; i++) {
            size[i] = 1;
        }

        int[] cityTree = new int[n + 1];
        cityTree[0] = -2;
        for (int i = 1; i < n + 1; i++) {
            cityTree[i] = -1;
        }

        for (int i = 0; i < cities_rows; i++) {
            unite(cities[i][0], cities[i][1], cityTree, size);
        }

        int numLib = 0;
        int numRoads = 0;
        for (int i = 1; i < cityTree.length; i++) {
            if (cityTree[i] == -1) {
                numLib++; // FOR EACH ROOT NODE, ADD A LIBRARY
                numRoads += (size[i] - 1); // FOR EACH ROOT NODE, FIND ITS SIZE - 1 AND ADD IT TO THE NUMBER OF ROADS
                                           // size of a tree = n - 1;
            }
        }

        return numLib * c_lib + numRoads * c_road;
    }

    // recursively finds the root of the tree containing the node containing value
    public static int find(int value, int jawn[]) {
        if (jawn[value] == -1) {
            return value;
        }
        return find(jawn[value], jawn);
    }

    public static void compress(int value, int jawn[], int root) {
        if (jawn[value] == -1) {
            jawn[value] = root;
            return;
        } else {
            int temp = jawn[value];
            jawn[value] = root;
            compress(temp, jawn, root);
        }
    }

    // unites subtrees
    public static void unite(int x, int y, int jawn[], int size[]) {
        // first do same component test
        int x1 = find(x, jawn);
        int y1 = find(y, jawn);
        if (x1 == y1)
            return;

        // if subtree containing x is smaller, attach to y
        if (size[x1] < size[y1]) {
            if (size[x1] > 1)
                compress(x, jawn, y1);
            else
                jawn[x1] = y1;
            size[y1] += size[x1];
        }

        // if subtree containing y is smaller, attach to x
        else {
            if (size[y1] > 1)
                compress(y, jawn, x1);
            else
                jawn[y1] = x1;
            size[x1] += size[y1];
        }
    }

}