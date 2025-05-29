""" 
https://leetcode.com/problems/third-maximum-number/description/?envType=problem-list-v2&envId=nh8lbv11
 """

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3 : 
            return nums[-1]
        return nums[-3]