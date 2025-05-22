""" 
https://leetcode.com/problems/linked-list-cycle/description/
 """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        table = {}

        cur = head 

        while cur : 
            if cur in table.keys() : 
                return True
            table[cur] = 1 
            cur = cur.next 
        
        return False
    
    # fast and slow pointer approach :
    # slow = fast = head 

    # while fast and fast.next : 
    #     fast = fast.next.next 
    #     slow = slow.next 
    #     if slow == fast : 
    #         return True
            
    # return False