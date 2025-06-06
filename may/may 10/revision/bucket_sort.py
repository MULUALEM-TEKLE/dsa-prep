def bucket_sort(arr) : 
    # construct bucket 
    bucket = [0] * (max(arr) +1) 
    for num in arr : 
        bucket[num] += 1

   
    # update array from bucket
    # i = 0
    # for n in range(len(bucket)) : 
    #     for _ in range(bucket[n]) : 
    #         arr[i] = n
    #         i += 1
    
    arr.clear()
    for i in range(len(bucket)): 
        arr.extend([i] * bucket[i])

    return arr


test_array = [2 , 1 , 2 , 0, 0, 2]
print(bucket_sort(test_array))