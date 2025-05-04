"""https://www.hackerrank.com/challenges/countingsort1/problem"""

""" def countingSort(arr):
    # Write your code here
    n = len(arr)
    counter_array = [0] * 100
    
    for num in arr : 
        if num in range(0 , n + 1) :
            counter_array[num] += 1
        
    
    return counter_array
 """



"""  def counting_sort(arr):
    max_range = max(arr)
    count = [0] * max_range + 1

    for num in arr:
        count[nums] += 1 

    result = []

    for i in range(len(count)):
        result.extend([i] * count[i])

    return result """


""" def counting_sort(arr):
    max_range = max(arr)
    count = [0] * (max_range + 1)

    for num in arr:
        count[nums] += 1 

    for i in range(1, len(count)):
        if count[i] > 1 : return i 
 """

 def two_pointer_sol(arr):
    # arr.sort()
    left = 0
    for right in range(1, len(arr)):
        if arr[right] == arr[right-1]:
            return arr[right]

        






    


