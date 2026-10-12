class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        H = [nums[0]]
        N = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            h = H[-1]
            H.append(max(nums[i], h * nums[i], N[-1] * nums[i]))
            N.append(min(nums[i], h * nums[i], N[-1] * nums[i]),)
        return max(H)