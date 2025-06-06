""" https://leetcode.com/problems/apply-operations-to-an-array/description/ """

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # perform operations 
        for i in range(len(nums) -1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0

        # shift zeros
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0 : 
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                
        return nums
        