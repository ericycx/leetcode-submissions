class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        smallest = 101
        second_smallest = 101
        for price in prices:
            if price < smallest:
                second_smallest = smallest
                smallest = price
            elif price < second_smallest:
                second_smallest = price
        total = money - (smallest + second_smallest)
        if  total >= 0:
            return total
        else:
            return money
            