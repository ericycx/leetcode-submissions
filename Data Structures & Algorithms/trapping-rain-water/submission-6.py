class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        prefix = []
        suffix = []
        pre_max = 0
        post_max = 0
        n = len(height)
        for i in range(n):
            pre_max = max(height[i],pre_max)
            prefix.append(pre_max)
        for j in range(n-1,-1,-1):
            post_max = max(height[j],post_max)
            suffix.append(post_max)
        for k in range(n):
            total += min(prefix[k],suffix[-k-1]) - height[k]
        return total
                