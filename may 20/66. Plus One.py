""" 
https://leetcode.com/problems/plus-one/
 """

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         number = 0
#         for i in range(len(digits)) : 
#             number += digits[i] * (10 ** (len(digits)-1 - i ))
        
#         number += 1

#         result = []

#         while number > 0 : 
#             digit = number % 10
#             number = number // 10
#             result.append(digit)
        
#         result.reverse()

#         return result 

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits) -1 , -1 , -1) : 
            res = digits[i] + 1
            if res >= 10 : 
                digits[i] = 0
                carry = 1
            else : 
                digits[i] = res
                return digits
            
        return [1] + digits
      
            