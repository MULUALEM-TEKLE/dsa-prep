import random
import time
def binary_search(arr, target) : 
    # initialize boundaries
    low , high = 0 , len(arr) - 1
    # while low is less than or equal to target
    while low <= high : 
        # find the mid point
        mid = (low + high)//2
        # if the target is greater than the mid point 
        if target > arr[mid] : 
            # make the mid point + 1 the new low while keeping the high
            low = mid + 1
        # if the target is less than the mid point 
        elif target < arr[mid]:
            # make the mid-1 point the new high while keepin g the low
            high = mid - 1
        # if target is the mid point
        else:
            # return the mid index
            return mid
    # if you get here with no value just return -1 b/c the item is not in the list
    return -1

""" 
Test driver implemented by gemini
 """

def run_test_case(arr, target):
    """Runs a single test case and prints the result. Returns True if passed, False otherwise."""
    print(f"Searching for {target} in {arr}")
    start_time = time.perf_counter()
    result = binary_search(arr, target)
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1_000_000  # in microseconds
    passed = False

    expected_index = -1
    if target in arr:
        expected_index = arr.index(target)

    if result == expected_index:
        print(f"Target {target} found at index {result} (Expected: {expected_index}) - PASSED")
        passed = True
    else:
        print(f"Target {target} found at index {result} (Expected: {expected_index}) - FAILED")

    print(f"Search took {duration:.2f} microseconds\n")
    return passed

def generate_sorted_array(size, min_val=0, max_val=1000):
    """Generates a sorted array of a given size with random integers."""
    arr = sorted(random.sample(range(min_val, max_val + 1), min(size, max_val - min_val + 1)))
    return arr

def generate_test_arrays(num_arrays=5, sizes=[10, 100, 1000, 10000, 100000], min_val=0, max_val=1000):
    """Generates a list of sorted test arrays with varying sizes."""
    test_arrays = []
    for size in sizes:
        test_arrays.append(generate_sorted_array(size, min_val, max_val))
    return test_arrays

def run_multiple_tests(test_arrays, num_targets_per_array=3):
    """Runs multiple test cases with different arrays and targets."""
    passed_count = 0
    failed_count = 0
    for arr in test_arrays:
        print(f"--- Testing array of size {len(arr)} ---")
        if not arr:
            target = random.randint(-10, 10)
            if run_test_case(arr, target):
                passed_count += 1
            else:
                failed_count += 1
            continue

        for _ in range(num_targets_per_array):
            # Test with existing element
            target_found = random.choice(arr)
            if run_test_case(arr, target_found):
                passed_count += 1
            else:
                failed_count += 1

            # Test with a non-existing element (within and outside range)
            min_val = arr[0]
            max_val = arr[-1]
            target_not_found1 = min_val - random.randint(1, 10)
            if run_test_case(arr, target_not_found1):
                passed_count += 1
            else:
                failed_count += 1
            target_not_found2 = max_val + random.randint(1, 10)
            if run_test_case(arr, target_not_found2):
                passed_count += 1
            else:
                failed_count += 1
    return passed_count, failed_count

def main():
    """Main function to run the binary search test driver with a final report."""
    passed_total = 0
    failed_total = 0

    print("--- Single Test Cases ---")
    tests_single = [
        ([2, 5, 7, 8, 11, 12], 11),
        ([2, 5, 7, 8, 11, 12], 5),
        ([2, 5, 7, 8, 11, 12], 1),
        ([2, 5, 7, 8, 11, 12], 15),
        ([], 5)
    ]
    for arr, target in tests_single:
        if run_test_case(arr, target):
            passed_total += 1
        else:
            failed_total += 1

    print("\n--- Multiple Test Cases with Varying Array Sizes ---")
    test_arrays = generate_test_arrays()
    passed_multiple, failed_multiple = run_multiple_tests(test_arrays)
    passed_total += passed_multiple
    failed_total += failed_multiple

    print("\n--- Final Report ---")
    print(f"Total Tests Passed: {passed_total}")
    print(f"Total Tests Failed: {failed_total}")
    if failed_total > 0:
        print("Binary Search implementation has some issues.")
    else:
        print("Binary Search implementation seems to be working correctly.")

if __name__ == "__main__":
    main()