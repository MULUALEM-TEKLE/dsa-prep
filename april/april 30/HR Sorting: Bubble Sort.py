"""
https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
"""


""" def countSwaps(a):
    swap_counter = 0
    # Write your code here
    for i in range(len(a)):
       for j in range(len(a) -1):
        if a[j] > a[j + 1] :
            a[j], a[j+1] = a[j+1] , a[j]
            swap_counter += 1
    print(f"Array is sorted in {swap_counter} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}") """

# alternative solution
""" def countSwaps(a):
    indexing_len = len(a) -1
    swap_counter = 0
    sorted = False
    while not sorted:
        sorted = True
        for i in range(indexing_len):
            if a[i] > a[i+1]:
                swap_counter += 1
                a[i], a[i+1] = a[i+1], a[i]
                sorted = False
    print(f"Array is sorted in {swap_counter} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
 """

# one more optimization
def bubble_sort(a):
    indexing_len = len(a) -1
    sorted = False
    sorted_last =0
    while not sorted:
        sorted = True
        for i in range(indexing_len - sorted_last ): # do not check last elements b/c they're sorted
            print(f"comparing {a[i]} and {a[i+1]}")
            if a[i] > a[i+1]:
                print(f"swapping {a[i]} and {a[i+1]}")
                a[i], a[i+1] = a[i+1], a[i]
                sorted = False
        sorted_last += 1

        print(f"iteration : {sorted_last} done")
        print(f"our array looks like this at the end of this iteration")
        print(a)
        print("===============================")
  


myArray = [9, 7, 4, 1, 2]
bubble_sort(myArray)




