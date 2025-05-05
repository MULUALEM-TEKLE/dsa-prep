""" 
https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/?envType=daily-question&envId=2025-05-04
 """

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = {}

        for domino in dominoes:
            domino.sort()
            key = str(domino)
        
            if key in freq.keys() :
                freq[key] += 1
            else :
                freq[key] = 1

        acc = 0
        for val in freq.values():
            if val > 1 : 
                acc += int((val * (val - 1)) /2)
           

        return acc
        