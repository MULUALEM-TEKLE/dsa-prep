import random 

def quick_sort(arr, s, e):
    if e - s + 1  <= 1 :
        return arr 

    piv = arr[e]
    left = s

    # for right in range(s, e):
    for right in range(s, e ):
        if arr[right] < piv  :
            arr[right] , arr[left] = arr[left], arr[right]
            left += 1

    arr[e] = arr[left]
    arr[left] = piv

    quick_sort(arr, s, left - 1)
    quick_sort(arr, left + 1 , e )

    return arr

# test_arr = [6 , 2, 1, 4, 3]
# quick_sort(test_arr, 0, len(test_arr) -1)

array_size = 10000
test_arr = [random.randint(0, 10000) for _ in range(array_size)]
my_sorted = quick_sort(test_arr, 0, len(test_arr) -1 )
python_sorted = sorted(test_arr) 

try : 
    assert python_sorted == my_sorted
    print("passed")
except : 
    print("fail")


