class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m, n = 0, len(nums) - 1
        boundary = nums[0]
        while m <= n:
            mid = (m + n) // 2
            if nums[mid] >= boundary:
                m = mid + 1
            else:
                n = mid - 1
        print(m,n)
        minimum_idx = m % len(nums)
        maximum_idx = n
        if target > nums[0]:
            m = 0
            n = maximum_idx
        elif target < nums[0]:
            m = minimum_idx
            n = len(nums) - 1
        else:
            return 0
        while m <= n:
            mid = (m + n) // 2
            if nums[mid] > target:
                n = mid - 1
            elif nums[mid] < target:
                m = mid + 1
            else:
                return mid
        return -1
