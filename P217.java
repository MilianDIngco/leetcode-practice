import java.util.HashMap;

public class P217 {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Boolean> numsSeen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (numsSeen.containsKey(nums[i]))
                return true;
            numsSeen.put(nums[i], true);
        }
        return false;
    }

}
