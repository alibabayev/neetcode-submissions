class MinStack:

    def __init__(self):
        self.stack = []
        minVal = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minVal = val
        else:
            difference = val - self.minVal
            self.stack.append(difference)
            if difference < 0:
                self.minVal = val
            

    def pop(self) -> None:
        if not self.stack:
            return 
            
        if self.stack[-1] < 0:
            self.minVal = self.minVal - self.stack[-1]
        self.stack.pop()

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.minVal
        else:
            return self.minVal + self.stack[-1]

    
    def getMin(self) -> int:
        return self.minVal
