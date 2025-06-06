def remove_middle_array(arr, i):
    for index in range(i+1, len(arr)):
        arr[index-1] = arr[index]
    arr[len(arr)-1] = None

array = [1, 2, 4, 5, 6, 22,42, 3,5, 23, 43, 23 ,11]
print(array)
remove_middle_array(array , 0 )
print(array)