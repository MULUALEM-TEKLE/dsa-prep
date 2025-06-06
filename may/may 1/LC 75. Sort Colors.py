""" https://leetcode.com/problems/sort-colors/ """

class Solution:
    def sortColors(self, nums) :
        max_range = max(nums) + 1
        counter = [0] * max_range

        for num in nums :
            counter[num] += 1
        print(counter)
        nums.clear()
        for i in range(len(counter)):
            nums.extend([i] * counter[i])
    
        """
        Do not return anything, modify nums in-place instead.
        """

sol = Solution()
sol.sortColors([2,0,2,1,1,0])

        