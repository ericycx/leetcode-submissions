class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def rec_search(nums,target,passed) -> int:
            if not nums:
                return -1
            start = len(nums) // 2
            if nums[start] == target:
                return passed + start
            elif nums[start] > target:
                return rec_search(nums[:start],target,passed)
            else:
                return rec_search(nums[start + 1:],target,passed + start + 1)

        return rec_search(nums,target, 0)



