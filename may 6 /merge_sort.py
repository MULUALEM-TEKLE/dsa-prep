import math
import random
import time

def merge(arr_one, arr_two):
    temp = [0] * (len(arr_one) + len(arr_two)) 
    # print(f"temp array len {len(temp)}")
    temp_ctr = 0
    arr_one_ptr = 0
    arr_two_ptr = 0

    while arr_one_ptr < len(arr_one) and arr_two_ptr < len(arr_two):
        if arr_one[arr_one_ptr] > arr_two[arr_two_ptr] :
            temp[temp_ctr] = arr_two[arr_two_ptr]
            arr_two_ptr += 1 
        else : 
            temp[temp_ctr] = arr_one[arr_one_ptr]
            arr_one_ptr += 1
        temp_ctr += 1 
        

    while arr_one_ptr < len(arr_one) : 
        temp[temp_ctr] = arr_one[arr_one_ptr]
        temp_ctr += 1 
        arr_one_ptr += 1 
       

    while arr_two_ptr < len(arr_two) : 
        temp[temp_ctr] = arr_two[arr_two_ptr]
        temp_ctr += 1 
        arr_two_ptr += 1 

    return temp
       

def merge_sort(arr,) : 

    if len(arr) <= 1:
        return arr
    
    mid_pt = len(arr)//2
    # print(f"mid point is {mid_pt}")
    arr_one = merge_sort(arr[ : mid_pt])
    arr_two =merge_sort(arr[mid_pt : ])

    return merge(arr_one, arr_two)

if __name__ == "__main__":
    # Create a large unsorted array
    large_array_size = 10  # Adjust the size as needed
    large_array = [random.randint(0, 10) for _ in range(large_array_size)]

    # Create a copy to test against Python's built-in sort
    python_sorted_array = sorted(large_array)

    # Measure the time taken by your merge sort
    start_time = time.time()
    your_sorted_array = merge_sort(list(large_array)) # Important: Sort a copy to avoid modifying the original
    end_time = time.time()
    your_merge_sort_time = end_time - start_time

    # Measure the time taken by Python's built-in sort
    start_time = time.time()
    _ = sorted(large_array)
    end_time = time.time()
    python_sort_time = end_time - start_time

    # Perform the assertion to check correctness
    try:
        assert your_sorted_array == python_sorted_array
        print(f"Merge sort test passed for an array of size {large_array_size}.")
        print(f"Your Merge Sort time: {your_merge_sort_time:.6f} seconds")
        print(f"Python's sorted() time: {python_sort_time:.6f} seconds")
        if your_merge_sort_time > python_sort_time * 5: # Heuristic to check for significant inefficiency
            print("Warning: Your merge sort seems significantly slower than Python's built-in sort. Consider potential optimizations.")
    except AssertionError:
        print(f"Merge sort test failed for an array of size {large_array_size}!")
        # If the test fails, you might want to inspect a smaller portion of the arrays
        # print("Your sorted array (first 20 elements):", your_sorted_array[:20])
        # print("Expected sorted array (first 20 elements):", python_sorted_array[:20])



    
