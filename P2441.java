public class P2441 {
    public static void main(String[] args) {
        int nums[] = { -1, 2, -3, 3 };
        System.out.println(findMaxK(nums));

    }

    public static int findMaxK(int[] nums) {
        sort(nums, 0, nums.length - 1);
        int l = 0, r = nums.length - 1;

        while (l < r && l < nums.length && r > 0) {
            if (Math.abs(nums[l]) == nums[r] & nums[l] < 0)
                return nums[r];
            if (Math.abs(nums[l]) > nums[r] & nums[l] < 0)
                l++;
            else
                r--;
        }

        return -1;
    }

    public static void merge(int[] arr, int l, int m, int r) {
        int n1 = m - l + 1;
        int n2 = r - m;

        int L[] = new int[n1];
        int R[] = new int[n2];

        for (int i = 0; i < n1; i++)
            L[i] = arr[l + i];
        for (int i = 0; i < n2; i++)
            R[i] = arr[m + 1 + i];

        int i = 0, j = 0, k = l;
        while (i < n1 && j < n2)
            arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];

        while (i < n1)
            arr[k++] = L[i++];
        while (j < n2)
            arr[k++] = R[j++];
    }

    public static void sort(int arr[], int l, int r) {
        if (l < r) {
            int m = l + (r - l) / 2;
            sort(arr, l, m);
            sort(arr, m + 1, r);

            merge(arr, l, m, r);
        }
    }

}
