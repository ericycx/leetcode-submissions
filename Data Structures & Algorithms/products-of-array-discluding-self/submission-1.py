class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lst = [1] * n

        # product before lst[i]
        prefix = 1
        for i in range(n):
            lst[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            lst[i] *= suffix
            suffix *= nums[i]
        return lst