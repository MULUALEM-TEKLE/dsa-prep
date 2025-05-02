"""
https://leetcode.com/problems/reorganize-string/description/
"""

def reorganizeString( s: str):
    word = list(s)
    print(word)
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            print(f"found similar items at index {i} and {i+1}")
            swap_found = False
            for j in range(1 , len(word)-1):
                if j-1 == 0 and word[j-1] != word[i+1] and word[j-1] != word[i] and word[j-1] != word[i+2] : 
                    word[j], word[i+1] = word[i+1], word[j]
                    swap_found = True
                    continue
                
                if j+1 == len(word) and  word[j+1] != word[i+1] and word[j+1] != word[i] and word[j+1] != word[i+2]:
                    word[j], word[i+1] = word[i+1], word[j]
                    swap_found = True
                    continue
                
                print(f'comparing {word[i+1]} at index {i+1} to the left with {word[j-1]} at index {j-1} and to the right with {word[j+1]} at index {j+1}')
                if word[j-1] != word[i+1] and word[j+1] != word[i+1] and word[j] != word[i] and word[j] != word[i+2] :
                    word[j], word[i+1] = word[i+1], word[j]
                    swap_found = True
                
                # print(f'comparing {word[i+1]} to the right with {word[j+1]} ')
                # if word[j+1] != word[i+1]:
                #     word[j], word[i+1] = word[i+1], word[j]
                    # swap_found = True
            if swap_found != True:
                return ""
    
    return "".join(word)

print(reorganizeString("baaba"))
# print(reorganizeString("aab"))
# print(reorganizeString("aab"))
