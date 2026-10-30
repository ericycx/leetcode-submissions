class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        total = 0
        res = float('inf')
        for j in range(len(nums)):
            total += nums[j]
            while total >= target:
                res = min(res, j - i  + 1)
                total -= nums[i]
                i += 1
        if res == float('inf'):
            return 0
        else:
             return res

