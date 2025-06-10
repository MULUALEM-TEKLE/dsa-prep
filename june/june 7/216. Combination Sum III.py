""" 
https://leetcode.com/problems/combination-sum-iii/
 """

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i , cur_sum) : 
            if cur_sum > n : 
                return 

            if len(subset) == k and cur_sum == n : 
                res.append(subset[:])
                return
            
            if i < 1 or len(subset) == k : 
                return
            
            subset.append(i)
            dfs(i-1, i + cur_sum)
            subset.pop()
            dfs(i-1 , cur_sum)
        
        dfs(9 , 0)
        return res