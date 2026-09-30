class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []
        product = 1
        more_than_1 = False
        for i in range(len(nums)):
            if nums[i] == 0:
                if more_than_1:
                    product = 0
                else:
                    more_than_1 = True
            else:
                product *= nums[i]
        for num in nums:
            if num == 0:
                lst.append(product)
            else:
                lst.append(product // num) if not more_than_1 else lst.append(0)
        return lst