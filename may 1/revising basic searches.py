unsorted_array_with_duplicates = [5, 1, 9, 3, 7, 2, 8, 4, 6, 5, 15, 11, 9, 13, 7, 12, 16, 10, 15, 4]
# bubble sort
def bubble(arr):
    passes = 0
    for i in range(len(arr)):
        for j in range(len(arr) - passes - 1 ):
            if arr[j] > arr[j+1] : 
                arr[j],  arr[j+1] =   arr[j+1],  arr[j]
        passes +=1 
    return  arr

# selection sort 
def selection(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1 , len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        if min_index != i:
            arr[i], arr[min_index] =  arr[min_index] , arr[i]

    return  arr

#insertion sort 
def insertion(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
           arr[j] , arr[j-1] = arr[j-1] , arr[j]
           j -= 1

    return  arr

# counting sort
def counting(arr):
    max_range = max(arr) + 1
    count = [0] * max_range
    # counting frequency
    for i in range(len(arr)):
        if arr[i] in range(max_range ):
            count[arr[i]] += 1
    result = []

    for i in range(len(count)):
        result.extend([i] * count[i])


    print(result )
    return  result


bubble_sorted = bubble(unsorted_array_with_duplicates[:])
selection_sorted = selection(unsorted_array_with_duplicates[:])
insertion_sorted = insertion(unsorted_array_with_duplicates[:])
counting_sorted = counting(unsorted_array_with_duplicates[:])

print(f"bubble sorted {bubble_sorted}")
print(f"selection sorted {selection_sorted}")
print(f"insertion sorted {insertion_sorted}")
print(f"counting sorted {counting_sorted}")

print(bubble_sorted == selection_sorted == insertion_sorted == counting_sorted )