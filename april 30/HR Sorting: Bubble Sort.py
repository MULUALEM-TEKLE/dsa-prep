"""
https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
"""


def countSwaps(a):
    swap_counter = 0
    # Write your code here
    for i in range(len(a)):
       for j in range(len(a) -1):
        if a[j] > a[j + 1] :
            a[j], a[j+1] = a[j+1] , a[j]
            swap_counter += 1
    print(f"Array is sorted in {swap_counter} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

# alternative solution
def countSwaps(a):
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




