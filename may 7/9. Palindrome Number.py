""" https://leetcode.com/problems/palindrome-number/description/ """

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False

        reversed = 0
        check = x
    
        while x > 0:
            reversed += (x%10) 
            if x < 10 :  break
            reversed *= 10
            x = x // 10

        return check == reversed
