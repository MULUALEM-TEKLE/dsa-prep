class Stack : 
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def peek(self):
        if len(self.stack) == 0 : return "Stack is empty"
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0
    
