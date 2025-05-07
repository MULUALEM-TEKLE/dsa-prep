class ListNode : 
    def __init__(self, val=0):
        self.val = val
        self.next = None

class LinkedList : 
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
    
    def push_start(self,val):
        new_node = ListNode(val)
        nxt = self.head.next
        self.head.next = new_node
        new_node.next = nxt
       
    
    def push_end(self, val):
        new_node = ListNode(val)
        new_node.next = self.tail
        cur = self.head
        while cur :
            if cur.next == self.tail:
               cur.next = new_node
               return
            cur = cur.next

    def print_list(self):
        list_string = ""
        cur = self.head.next

        while cur != self.tail : 
            list_string += f"{cur.val} -> "
            cur = cur.next

        print(list_string)

test_list = LinkedList()
test_list.push_end(1)
test_list.push_start(666)
test_list.push_end(888)
test_list.print_list()

