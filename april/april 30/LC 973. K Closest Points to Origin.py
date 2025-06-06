"""
https://leetcode.com/problems/k-closest-points-to-origin/description/
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sqrt_list = [(i[0]**2 + i[1]**2) for i in points]
        table = {}

        for i in range(len(sqrt_list)):
            if sqrt_list[i] in table:
                table[sqrt_list[i]].append(i)
            else:
                table[sqrt_list[i]] = [i]
         
        finalists = sorted(table.keys())[:k]
       

        temp = []
        for i in range(k): 
            if not len(temp) >= k:
                temp.extend(table[finalists[i]])
                          
        return [points[temp[i]] for i in range(len(temp))]

        
# import heapq
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         squared_list = [(point[0] ** 2  + point[1] ** 2) for point in points]
#         table = {}
#         for index , square in enumerate(squared_list) : 
#             if square in table.keys() : 
#                 table[square].append(points[index])
#             else :
#                 table[square] = [points[index]]

#         heapq.heapify(squared_list)
#         min = set(heapq.nsmallest(k , squared_list))
#         res = []
#         for m in min : 
#             res.extend(table[m])

#         return res