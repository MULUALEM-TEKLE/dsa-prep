"""
https://leetcode.com/problems/k-closest-points-to-origin/description/
"""
# time limit exeeded
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        sqrt_list = [0] * len(points)
        for i in range(n):
            sqrt_list[i] = points[i][0] ** 2 +  points[i][1] ** 2

        for i in range(n):
            for j in range(1 , n):
                if sqrt_list[j] < sqrt_list[j-1]:
                    sqrt_list[j], sqrt_list[j-1], points[j], points[j-1] = sqrt_list[j-1], sqrt_list[j], points[j-1], points[j]
                    j -= 1
        
        return points[:k]