""" 
https://leetcode.com/problems/valid-palindrome/description/
 """

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join([char.lower() for char in s if char.isalnum()])
        if clean == "" : 
            return True
        left = 0
        right = -1
        while left <= len(clean) // 2  : 
            if clean[left] != clean[right] : 
                return False

            left += 1
            right -= 1

        return True