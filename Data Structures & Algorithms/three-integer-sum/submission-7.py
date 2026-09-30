class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = []
        # you iterate through each element in the list then two pointers
        nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            j = i + 1
            k = n - 1
            if i != 0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    triples.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return triples