import random
def counting_sort(arr):    
    max_num = max(arr)
    count = [0] * (max_num + 1)

    # count
    for num in arr:
        count[num] += 1

    # cumulative add to the right
    for i in range(1, len(count)):
        count[i] += count[i-1]

    output = [0] * (len(arr))

    for i in range(0, len(arr)):
        output[count[arr[i]] - 1 ] = arr[i]
        count[arr[i]] -= 1 

    return output

large_array_size = 10000
max_value = 500  # Keep the range relatively small for counting sort efficiency
large_array = [random.randint(0, max_value) for _ in range(large_array_size)]

# Create a copy to use for the assertion
expected_sorted_array = sorted(large_array)

# Sort the array using the counting sort function
actual_sorted_array = counting_sort(large_array)

# Assertion to test if the counting sort function worked correctly
try:
    assert actual_sorted_array == expected_sorted_array
    print(f"Counting sort test passed for an array of size {large_array_size}.")
except AssertionError:
    print(f"Counting sort test failed for an array of size {large_array_size}!")
    # You might want to print the arrays to debug further if the assertion fails
    # print("Expected:", expected_sorted_array[:20]) # Print first 20 elements
    # print("Actual:", actual_sorted_array[:20])   # Print first 20 elements
