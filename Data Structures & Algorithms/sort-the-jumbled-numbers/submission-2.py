class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            mapped = int(''.join(str(mapping[int(d)]) for d in str(num)))
            res.append((mapped, i))
        res.sort()
        return [nums[i] for _, i in res]

