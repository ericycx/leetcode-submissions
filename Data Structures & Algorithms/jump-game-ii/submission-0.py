class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        prev = 0
        counter = 0                      # last index already scanned (absolute)
        while i < n - 1:
            counter += 1
            end = i + nums[i]         # farthest index reachable from i (absolute)
            if end >= n - 1:
                return counter
            new_i = i
            for j in range(prev + 1, end + 1):        # only unscanned indices
                if j + nums[j] > new_i + nums[new_i]:
                    new_i = j
            if new_i == i:            # nothing in range reaches past end
                return False
            prev = end
            i = new_i
        return counter