class Node :
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList :
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def insert_end(self, val):
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node
    
    def remove(self, index):
        cur = self.head
        i = 0

        while cur and i < index :
            i+=1
            cur = cur.next

        if cur : 
            cur.next = cur.next.next

    def print_list(self):
        cur = self.head.next
        list = ""

        while cur:
            list += (f"{cur.val}  ==> ")
            cur = cur.next
        print(list)

test_list = LinkedList()

test_list.insert_end(1)
test_list.insert_end(2)
test_list.insert_end(3)
test_list.insert_end(4)
test_list.insert_end(5)

test_list.remove(3)



test_list.print_list()