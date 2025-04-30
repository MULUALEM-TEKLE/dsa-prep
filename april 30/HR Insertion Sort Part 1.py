"""
https://www.hackerrank.com/challenges/insertionsort1/problem
"""
# problem is a bit unusual, still figuring it out 

# my approach for a normal insertion sort
array = [2,4,6,8,3]
def insertion_sort(arr):
    for i in range(len(arr)):
        j=i
        while j> 0 and arr[j] < arr[j-1] :
            arr[j] , arr[j-1] = arr[j-1], arr[j]
            j -=1
    print(arr)
    return arr

insertion_sort(array)
