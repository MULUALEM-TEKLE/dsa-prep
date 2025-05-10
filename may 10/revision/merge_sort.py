def merge(arr, s, m, e) : 
    # copy the left and right parts
    L = arr[s:m+1]
    R = arr[m+1 : e+1]
    # initialize pointers for left, right and main array
    i = j = 0
    k = s
    # merging left and right
    while i < len(L) and j < len(R) : 
        if L[i] <= R[j] : 
            arr[k] = L[i]
            i += 1 
        else : 
            arr[k] = R[j]
            j += 1
        k += 1
    # padding with left
    while i < len(L) : 
        arr[k] = L[i]
        i += 1 
        k += 1

    # padding with right
    while  j < len(R) : 
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, s, e): 
    # base case
    if (e - s + 1) <= 1 : 
        return arr
    
    # finding the middle
    m = (s+e)//2

    # recursive case
    # merge first half
    merge_sort(arr, s, m)
    # merge second half
    merge_sort(arr, m+1, e)

    # merge
    merge(arr, s, m, e)

    return arr


test_array = [3,2,4,6,1]
test_array = merge_sort(test_array, 0, 4)
print(test_array)