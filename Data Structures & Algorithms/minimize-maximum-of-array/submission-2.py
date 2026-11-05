class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = 0
        cur_max = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if nums[i] >= cur_max or nums[i] >= res:
                cur_max = nums[i]
                res = max(res, math.ceil(total / (i+1)))
        return res

            