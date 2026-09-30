class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        n = len(nums)
        for i in range(n):
            compliment = target - nums[i]
            if compliment in hashMap:
                return [hashMap[compliment], i]
            hashMap[nums[i]] = i