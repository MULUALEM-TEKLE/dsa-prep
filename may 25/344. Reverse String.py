""" 
https://leetcode.com/problems/reverse-string/description/?envType=problem-list-v2&envId=nh8lbv11
 """

class Solution:
    def reverseString(self, s: List[str]) -> None:

        """
        Do not return anything, modify s in-place instead.
        """
        left , right = 0 , len(s) - 1

        while left <= right : 
            s[left] , s[right] = s[right] , s[left]
            left += 1 
            right -= 1 

        