class Solution:
    def findMin(self, nums: List[int]) -> int:
        m, n = 0, len(nums) - 1
        boundary = nums[0]
        while m <= n:
            mid = (m + n) // 2
            if nums[mid] >= boundary:
                m = mid + 1
            else:
                n = mid - 1
        return nums[m % len(nums)]



