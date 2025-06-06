"""https://leetcode.com/problems/valid-parentheses/description/"""

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()
    
    def peek(self):
        return self.stack[len(self.stack)-1]
    
    def is_empty(self):
        return len(self.stack) == 0

class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        stack = Stack()

        for s in s_list:
            if s == "(" or s== "[" or s== "{":
                stack.push(s)

            else:
                if stack.is_empty() : return False
                top = stack.peek()
                if (s == ")" and top == "(") or (s == "]" and top == "[") or (s == "}" and top == "{") : 
                    stack.pop()
                else : 
                    return False
        
        return stack.is_empty()

        