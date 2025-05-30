""" https://leetcode.com/problems/min-stack/description/ """
class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        i = 0
        min = self.stack[i]
        for j in range(i+1, len(self.stack)):
            if self.stack[j] < min: 
                min = self.stack[j]
            i += 1
        return min