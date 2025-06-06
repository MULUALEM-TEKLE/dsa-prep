
def binary_search_range(low, high): 
    while low <= high : 
        mid = (low + high) // 2
        # we're basically guessing if the number is in the range 
        if check_function(mid) > 0 : 
            high = mid - 1 
        elif check_function(mid) < 0 : 
            low = mid + 1
        else :
            return mid 
    return -1

# this can be a black box function since we're looking for the secret number
def check_function(n) : 
    if n > 10 : 
        return 1
    elif n < 10 : 
        return -1
    else : 
        return 0
    

print(binary_search_range(11, 100))