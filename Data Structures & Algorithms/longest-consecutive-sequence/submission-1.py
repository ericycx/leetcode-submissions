class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1 pass
        max_count = 0
        # if you check a sequence it also checks for all in consecutive with it
        new_Set = set(nums)
        for i in range(len(nums)):
            if nums[i] - 1 not in new_Set:
                count = 1
                cur = nums[i]
                while cur + 1 in new_Set:
                    cur += 1
                    count += 1
                max_count = max(max_count, count)

        return max_count