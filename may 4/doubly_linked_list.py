class Node:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None

class DLinkedList():
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_start(self, val):
        new_node = Node(val)

        new_node.prev = self.head
        new_node.next = self.head.next 

        self.head.next.prev = new_node
        self.head.next = new_node

    def remove_start(self):
        self.head.next = self.head.next.next
        self.head.next.next.prev = self.head

    def insert_end(self, val):
        new_node = Node(val)

        new_node.next = self.tail
        new_node.prev = self.tail.prev

        self.tail.prev.next = new_node
        self.tail.prev = new_node

       
    def remove_end(self):
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.prev.next = self.tail

    def print_list(self):
        cur = self.head.next
        lst = ""
        while cur != self.tail:
            lst += f"{cur.val} => "
            cur = cur.next
        print(lst)

test_list = DLinkedList()

test_list.insert_start(1)
test_list.insert_start(2)
test_list.insert_start(3)
test_list.insert_start(4)



test_list.insert_end(11)
test_list.insert_end(12)
test_list.insert_end(13)
test_list.insert_end(14)

test_list.print_list()
test_list.remove_start()
print("after removing start")
test_list.print_list()

test_list.remove_end()
print("after removing end")
test_list.print_list()