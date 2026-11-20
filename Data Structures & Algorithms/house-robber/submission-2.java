class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];

        int[] H = new int[n];
        H[0] = nums[0];
        H[1] = Math.max(nums[0], nums[1]);
        for (int i = 2; i < n; i++) {
            H[i] = Math.max(H[i - 1], H[i - 2] + nums[i]);
        }
        return H[n - 1];
    }
}