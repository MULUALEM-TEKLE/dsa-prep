""" 
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/solutions/1054370/python-3-swapping-nodes-swapping-values-one-pass-fully-explained/
 """
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # array = []
        # cur = head
        # while cur :
        #     array.append(cur.val)
        #     cur = cur.next
        
        # array[k -1], array[-k] = array[-k] , array[k -1]

        # dummy = ListNode()
        # cur = dummy 
        # for num in array:
        #     cur.next = ListNode(num)
        #     cur = cur.next

        # return dummy.next

        cur = head 
        for i in range(k-1) : 
            cur = cur.next

        right = head 
        left = cur 

        while cur.next : 
            cur = cur.next 
            right = right.next 

        right.val , left.val = left.val, right.val
        return head
        