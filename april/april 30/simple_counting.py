def simple_counting_sort(arr):
    """
    A simpler version of counting sort for non-negative integers.
    Note: This version is not stable.
    """
    # Check if the input array is empty. If it is, return an empty list as there's nothing to sort.
    if not arr:
        return []

    # Find the maximum value in the input array. This determines the range of our counting array.
    max_val = max(arr)

    # Create a 'count' array (list) with a size of 'max_val + 1', initialized with zeros.
    # Each index in this 'count' array will represent a number from 0 to max_val,
    # and the value at that index will store the frequency of that number in the input array.
    count = [0] * (max_val + 1)

    # Initialize an empty list called 'output'. This list will store the sorted elements.
    output = []

    # Iterate through each number in the input array 'arr'.
    for num in arr:
        # For each 'num', increment the count at the index corresponding to that number in the 'count' array.
        # For example, if 'num' is 3, we increment count[3] by 1.
        # This step essentially counts the occurrences of each unique number in 'arr'.
        count[num] += 1

    # Print the 'count' array (for demonstration purposes to see the frequencies).
    # After this loop, count[i] will hold the number of times the value 'i' appeared in 'arr'.
    print(count)

    # Iterate through the 'count' array from index 0 to max_val (inclusive).
    for i in range(len(count)):
        # For each index 'i' (which represents a number), the value 'count[i]' tells us
        # how many times that number appeared in the original array.
        # We now append the number 'i' to the 'output' array 'count[i]' times.
        # For example, if count[2] is 3, we append the number 2 to 'output' three times.
        output.extend([i] * count[i])

    # Return the 'output' list, which now contains all the elements from the input array 'arr' in sorted order.
    return output

# Example usage:
my_array = [4, 2, 2, 8, 3, 3, 1]
sorted_array = simple_counting_sort(my_array)
print(sorted_array)

another_array = [0, 5, 1, 0, 3, 5, 2]
sorted_another = simple_counting_sort(another_array)
print(sorted_another)