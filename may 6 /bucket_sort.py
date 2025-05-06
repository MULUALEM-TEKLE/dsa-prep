import random

def bucket_sort(arr) : 
    max_range = max(arr)
    bucket = [0] * (max_range + 1)

    for num in arr : 
        bucket[num] += 1

    i = 0
    for n in range(len(bucket)) :
        for _ in range(bucket[n]):
            arr[i] = n
            i += 1
    
    return arr

def generate_bucket_sort_test_array(length=20, min_val=0, max_val=9):
    """Generates a test array for bucket sort within a specified range."""
    return [random.randint(min_val, max_val) for _ in range(length)]

# Generate the test array
test_array = generate_bucket_sort_test_array(length=2000, min_val=0, max_val=1540)
# print(test_array)
my_sorted = bucket_sort(test_array)
python_sorted = sorted(test_array)

try : 
    assert my_sorted == python_sorted 
    print("passed")
except : 
    print("failed")