"""
https://leetcode.com/problems/find-target-indices-after-sorting-array/description/
"""

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        target_array =[]
        for i in range(len(nums)):
            j=i
            while j>0 and nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j-=1
        
        for i in range(len(nums)):
            if nums[i] == target: 
                target_array.append(i)
        
        return target_array