""" 
https://leetcode.com/problems/kth-missing-positive-number/?envType=problem-list-v2&envId=nh8idze7
 """
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # bruteforce approach
        for i in range(1 , max(arr) + k + 1 ) : 
            if i not in arr : 
                k -= 1 
                if k == 0 : 
                    return i
                
        # binary search approach
        
        # low , high = 0 , len(arr) 

        # while low < high : 
        #     mid = (low + high)//2

        #     if (arr[mid] - mid - 1) < k : 
        #         low = mid + 1 
        #     else : 
        #         high = mid
        
        # return low + k