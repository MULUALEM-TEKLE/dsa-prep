"""
https://leetcode.com/problems/sorting-the-sentence/description/
"""

class Solution:
    def sortSentence(self, s: str) -> str:
        sentence_list = s.split(" ")
        
        ordered_sentence_list = [" "] * len(sentence_list)
        for word in sentence_list:
            ordered_sentence_list[int(word[-1]) -1] = word[:-1]
        return " ".join(ordered_sentence_list)

        """
        Input: s = "is2 sentence4 This1 a3"
        Output: "This is a sentence"
        """