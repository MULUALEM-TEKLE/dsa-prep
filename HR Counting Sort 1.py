"""https://www.hackerrank.com/challenges/countingsort1/problem"""

def countingSort(arr):
    # Write your code here
    n = len(arr)
    counter_array = [0] * 100
    
    for num in arr : 
        if num in range(0 , n + 1) :
            counter_array[num] += 1
    return counter_array