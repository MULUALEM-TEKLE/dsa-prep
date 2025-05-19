""" 
https://leetcode.com/problems/kth-largest-element-in-an-array/description/
 """

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k , nums)[-1]