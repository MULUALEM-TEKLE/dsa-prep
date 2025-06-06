def quick_sort(arr, s, e) : 
    # base case
    if e - s +1  <= 1:
        return arr
    # selecting a pivot
    p = arr[e]
    left = s
    # partitioning
    for i in range(s, e) : 
        if arr[i] < p : # move everything less than pivot to the left 
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
    # moving pivot to partition end | to the boundary of the partition
    arr[e] = arr[left]
    arr[left] = p

    # recursive case
    # sort left
    quick_sort(arr , s, left - 1) # not touching left because its already in its place
    # sort right
    quick_sort(arr , left + 1, e) # not touching left because its already in its place
    # return sorted

    return arr

test_array = [3,2,4,6,1]
test_array = quick_sort(test_array, 0, 4)
print(test_array)