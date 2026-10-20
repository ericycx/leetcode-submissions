class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        H = [-999999] *  (n + 1)
        H[0] = nums[0]
        for i in range(1, n):
            H[i] = max(H[i - 1] + nums[i], nums[i])
        return max(H)