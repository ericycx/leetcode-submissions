class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        local = 0
        for num in nums:
            if num != 1:
                count = max(local, count)
                local = 0
            else:
                local += 1
        return max(count, local)