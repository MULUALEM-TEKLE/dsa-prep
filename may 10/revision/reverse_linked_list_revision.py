class ListNode : 
    def __init__(self, val = -1):
        self.val = val
        self.next = None

class LinkedList: 
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head
        

    def push(self, val) : 
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def pop(self) : 
        ret = None
        c = self.head
        while c :
            if c.next == self.tail :
                ret = c.next
                self.tail = c
                break   
            c = c.next
        return ret.val
    
    def top(self) : 
        return self.tail.val
    
    def is_empty(self):
        return self.head.next == None
    
    def print_list(self) :
        list_str = ""
        c = self.head.next
        while c :
            list_str += f"{c.val} ->"
            c = c.next
        print(list_str[:-3])

def reverseLinkedList(lst): 
    left = None
    right = lst

    while right : 
        tmp = right.next
        right.next = left
        left = right 
        right = tmp

    
    
    return left
    

test = LinkedList()
test.push(1)
test.push(2)
test.push(3)
test.push(21)
test.push(32)
test.push(43)
test.print_list()
test.head = reverseLinkedList(test.head)
test.print_list()

    
 


