class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if stack:
                while stack and temperatures[i] > stack[-1][0]:
                    comparison = stack.pop()
                    result[comparison[1]] = i - comparison[1]
            stack.append((temperatures[i],i))
        return result