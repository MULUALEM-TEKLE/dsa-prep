"""
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/?envType=daily-question&envId=2025-04-30
"""


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # solution one
        """
        even_num_counter = 0
        for num in nums :
            if len(str(num)) %2 == 0 :
                even_num_counter += 1
        return even_num_counter
        """
        # solution two
        """
        even_num_counter = 0
        for num in nums :
            digit = 0
            while num > 0:
                digit += 1
                num //= 10
            if digit % 2 == 0 :
                even_num_counter += 1
        return even_num_counter
        """
        # solution three | found this from youtube
        even_num_counter = 0
        for num in nums :
            if (num >= 10 and num <= 99) or (num >= 1000 and num <=9999) or (num == 100000) :
                even_num_counter +=1
        return even_num_counter




