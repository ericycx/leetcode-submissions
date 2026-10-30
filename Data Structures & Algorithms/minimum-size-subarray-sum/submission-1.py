class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        total = 0
        res = 999999999
        for j in range(len(nums)):
            if total < target:
                total += nums[j]
            while total >= target:
                print(i,j)
                res = min(res, j - i  + 1)
                total -= nums[i]
                i += 1
        if i == 0:
            return 0
        else:
             return res

