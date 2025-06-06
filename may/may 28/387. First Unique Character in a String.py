""" 
https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=nh8lbv11
 """

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = defaultdict(int)

        for letter in s : 
            freq[letter] += 1 
        
        for index , letter in enumerate(s) : 
            if freq[letter] == 1 : 
                return index

        return -1