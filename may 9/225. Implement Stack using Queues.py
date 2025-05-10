""" 
https://leetcode.com/problems/implement-stack-using-queues/description/
 """

# attempted 
class QueueNode : 
    def __init__(self, val = -1): 
        self.val = val 
        self.next = None

class Queue: 
    def __init__(self) : 
        self.head = QueueNode()
        self.tail = self.head

    def top(self) :
        if self.head.next == None : 
            return None
        return self.head.next.val

    def enqueue(self, val) : 
        new_node = QueueNode(val)
        self.tail.next = new_node
        self.tail = new_node
      

    def dequeue(self) : 
        if self.head.next == None : 
            return None
        ret = self.head.next.val
        self.head.next = self.head.next.next
        if self.head.next is None:
            self.tail = self.head  # Update tail when queue becomes empty
        return ret
    
    def size(self) : 
        size = 0
        cur = self.head.next
        while cur != self.tail : 
            size += 1
            cur = cur.next

        return size

    def print_queue(self) : 
        if self.head.next == None : 
            print("empty")
            return None
        q = ""
        cur = self.head.next 
        while cur: 
            q += f"{cur.val} ->"
            cur = cur.next
        print(q[: -3])
        

class MyStack:

    def __init__(self):
        self.stack = Queue()
        

    def push(self, x: int) -> None:
        self.stack.enqueue(x)

    def pop(self) -> int:
        s = 0
        while s < self.stack.size() - 1 : 
            self.stack.enqueue(self.stack.dequeue())
            s += 1
        return self.stack.dequeue()

    def top(self) -> int:
        return self.stack.tail.val
        
    def empty(self) -> bool:
        return self.stack.head.next == None
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()