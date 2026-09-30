class MinStack:

    def __init__(self):
        self.items = []
        self.min = []
        

    def push(self, val: int) -> None:

        self.items.append(val)
        if self.min:
            self.min.append(min(val,self.min[-1]))
        else:
            self.min.append(val)
        
    def pop(self) -> None:
        self.items.pop()
        self.min.pop()
        

    def top(self) -> int:
        return self.items[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        
