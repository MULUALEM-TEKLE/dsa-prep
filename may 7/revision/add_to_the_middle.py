def add_to_middle(arr, index, val, len) : 
    for index in range(len - 1,  index -1 , -1):
        arr[index+1] = arr[index]
    
    arr[index] = val

array = [1, 2, 4, 5, 6, 22,42, 3,5, 23, 43, 23 ,11, 0 , 0] # the zeros at the end are just padding as empty space to shift stuff into
print(array)
add_to_middle(array , 6 , 666, 13 )
print(array)