class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        local_count = 0
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                local_count += 1
            while local_count > k:
                if nums[i] == 0:
                    local_count -= 1
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res