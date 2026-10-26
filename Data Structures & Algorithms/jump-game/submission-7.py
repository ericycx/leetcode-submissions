class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        prev = 0                      # last index already scanned (absolute)
        while i < n - 1:
            end = i + nums[i]         # farthest index reachable from i (absolute)
            if end >= n - 1:
                return True
            new_i = i
            for j in range(prev + 1, end + 1):        # only unscanned indices
                if j + nums[j] > new_i + nums[new_i]:
                    new_i = j
            if new_i == i:            # nothing in range reaches past end
                return False
            prev = end
            i = new_i
        return True