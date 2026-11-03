class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            num = nums[i]
            mapped = ''
            for digit in str(num):
                mapped = mapped + str(mapping[int(digit)])
            res.append((int(mapped), i))
        res.sort()
        return [nums[res[i][1]] for i in range(len(nums))] 

