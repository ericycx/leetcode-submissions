class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        self.stack.append(price)
        copy = self.stack[:]
        count = 0
        while copy and copy[-1] <= price:
            count += 1
            copy.pop()
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)