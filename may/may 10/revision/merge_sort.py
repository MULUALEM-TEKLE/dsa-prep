def merge(array, start_index, middle_index, end_index):
    """
    Merges two sorted subarrays into a single sorted subarray.

    Args:
        array: The array containing the subarrays to be merged.
        start_index: The starting index of the first subarray.
        middle_index: The ending index of the first subarray (and the starting index - 1 of the second).
        end_index: The ending index of the second subarray.
    """
    # Create copies of the left and right subarrays to avoid modifying the original array directly during the merge.
    left_array = array[start_index:middle_index + 1]  # Copy of the left subarray
    right_array = array[middle_index + 1:end_index + 1]  # Copy of the right subarray

    # Initialize pointers for the left and right subarrays, and for the merged array.
    left_pointer = 0
    right_pointer = 0
    merged_pointer = start_index

    # Merge the left and right subarrays, comparing elements and placing them in order into the merged array.
    while left_pointer < len(left_array) and right_pointer < len(right_array):
        if left_array[left_pointer] <= right_array[right_pointer]:
            array[merged_pointer] = left_array[left_pointer]
            left_pointer += 1
        else:
            array[merged_pointer] = right_array[right_pointer]
            right_pointer += 1
        merged_pointer += 1

    # If the left subarray has remaining elements, add them to the merged array.
    while left_pointer < len(left_array):
        array[merged_pointer] = left_array[left_pointer]
        left_pointer += 1
        merged_pointer += 1

    # If the right subarray has remaining elements, add them to the merged array.
    while right_pointer < len(right_array):
        array[merged_pointer] = right_array[right_pointer]
        right_pointer += 1
        merged_pointer += 1



def merge_sort(array, start_index, end_index):
    """
    Sorts an array using the Merge Sort algorithm.

    Args:
        array: The array to be sorted.
        start_index: The starting index of the portion of the array to be sorted.
        end_index: The ending index of the portion of the array to be sorted.

    Returns:
        The sorted array.  Note that the array is sorted in place, but it is also returned for convenience.
    """
    # Base case: If the subarray has 0 or 1 elements, it is already sorted.
    if (end_index - start_index + 1) <= 1:
        return array  # Return for consistency, though the array is modified in place

    # Recursive case:
    # 1. Find the middle index of the subarray.
    middle_index = (start_index + end_index) // 2

    # 2. Recursively sort the left subarray.
    merge_sort(array, start_index, middle_index)

    # 3. Recursively sort the right subarray.
    merge_sort(array, middle_index + 1, end_index)

    # 4. Merge the sorted left and right subarrays.
    merge(array, start_index, middle_index, end_index)

    return array # Returns the sorted array

if __name__ == '__main__':
    test_array = [5, 2, 9, 1, 5, 6]
    sorted_array = merge_sort(test_array, 0, len(test_array) - 1)
    print("Sorted array:", sorted_array)  # Output: Sorted array: [1, 2, 5, 5, 6, 9]

    test_array_2 = [10, 7, 8, 9, 1, 5]
    sorted_array_2 = merge_sort(test_array_2, 0, len(test_array_2) -1)
    print("Sorted array:", sorted_array_2)
