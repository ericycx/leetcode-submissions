class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        counter = 0
        prev = 0
        while i < (n-1) and counter < n:
            print(i)
            dist = nums[i]
            new_i = dist
            for jumps in range(dist - prev, min(dist, n - i - dist)):
                if jumps + nums[i + jumps] > new_i + nums[i + new_i]:
                    new_i = jumps
            prev = i
            i += new_i
            counter += 1
        return (i >= (n-1)) 