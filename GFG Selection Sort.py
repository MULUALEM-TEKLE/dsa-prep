"""
https://www.geeksforgeeks.org/problems/selection-sort/1
"""

#User function Template for python3

class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(0, len(arr)):
            min_index = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]
                
        # print(*arr)
        # return arr
                