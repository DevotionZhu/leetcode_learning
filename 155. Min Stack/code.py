class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_num = 4294967296

    def push(self, x):
        self.stack.append(x)
        if x < self.min_num:
            self.min_num = x

    def pop(self):
        if self.stack:
            x = self.stack.pop()
            if x <= self.min_num:
                if self.stack:
                    self.min_num = min(self.stack)
                else:
                    self.min_num = 4294967296

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.stack and self.min_num != 4294967296:
            return self.min_num
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
