class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n < 2:
            return nums[0]
        H = [-1] * (n + 1)
        H[0] = nums[0]
        H[1] = max(nums[0], nums[1])
        for i in range(2, n):
            H[i] = max(H[i-1], H[i-2] + nums[i])
        return H[n-1]