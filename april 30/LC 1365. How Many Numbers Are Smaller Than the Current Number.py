"""
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j or nums[i] == nums[j]:
                    continue
                if nums[j] < nums[i] : 
                    output[i] += 1
        return output
        