class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # calculate current every time you reset lowest
        # max is equal to max(current, max)
        maxP = 0
        if not prices:
            return maxP
        highest = prices[0]
        lowest = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < lowest:
                curP = highest - lowest
                maxP = max(curP, maxP)
                lowest = prices[i]
                highest = prices[i]
            highest = max(prices[i],highest)
        return max(maxP, highest-lowest)
        
