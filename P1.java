import java.util.HashMap;

public class P1 {

    public static void main(String[] args) {
        P1 a = new P1();
        int[] arr = { 1, 2, 3, 4, 5 };
        a.twoSum(arr, 4);
    }

    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<>();
        int[] sol = new int[2];

        for (int i = 0; i < nums.length; i++) {
            sol[0] = i;
            if (!seen.isEmpty() && seen.containsKey(target - nums[sol[0]])) {
                sol[1] = seen.get(target - nums[sol[0]]);
                System.out.println(sol[0] + " " + sol[1]);
                return sol;
            }
            seen.put(nums[i], i);
        }

        return sol;
    }
}
