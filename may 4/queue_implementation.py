class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def enqueue(self, val):
        new_node = Node(val)
        
        new_node.next = self.tail
        new_node.prev = self.tail.prev

        self.tail.prev.next = new_node
        self.tail.prev = new_node


    def dequeue(self):
        dq = self.head.next.val

        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

        return dq 

    def print_queue(self):
        cur = self.head.next
        q = ""
        while cur != self.tail : 
            q += f"{cur.val} => "
            cur = cur.next
        print(q)
            


test_queue = Queue()

test_queue.enqueue(1)
test_queue.enqueue(3)
test_queue.enqueue(5)
test_queue.enqueue(6)

# test_queue.print_queue()
print(test_queue.dequeue())
# test_queue.print_queue()
print(test_queue.dequeue())
# test_queue.print_queue()
print(test_queue.dequeue())
# test_queue.print_queue()

test_queue.enqueue(11)
test_queue.enqueue(13)
test_queue.enqueue(51)
test_queue.enqueue(16)
test_queue.print_queue()
print(test_queue.dequeue())



