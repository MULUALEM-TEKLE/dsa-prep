"""
https://leetcode.com/problems/two-sum/description/
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = [0 , 0]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target-nums[i]:
                    output[0] , output[1] = i, j
        return output