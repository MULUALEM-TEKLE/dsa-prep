"""Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

Array is sorted in numSwaps swaps., where  is the number of swaps that took place.
First Element: firstElement, where  is the first element in the sorted array.
Last Element: lastElement, where  is the last element in the sorted array.
Hint: To complete this challenge, you must add a variable that keeps a running tally of all swaps that occur during execution.

Example

swap    a
0       [6,4,1]
1       [4,6,1]
2       [4,1,6]
3       [1,4,6]
The steps of the bubble sort are shown above. It took  swaps to sort the array. Output is:

Array is sorted in 3 swaps.
First Element: 1
Last Element: 6
Function Description

Complete the function countSwaps in the editor below.

countSwaps has the following parameter(s):

int a[n]: an array of integers to sort
Prints

Print the three lines required, then return. No return value is expected.

Input Format

The first line contains an integer, , the size of the array .
The second line contains  space-separated integers .

Constraints

Output Format

Sample Input 0

STDIN   Function
-----   --------
3       a[] size n = 3
1 2 3   a = [1, 2, 3]
Sample Output 0

Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
Explanation 0
The array is already sorted, so  swaps take place.

Sample Input 1

3
3 2 1
Sample Output 1

Array is sorted in 3 swaps.
First Element: 1
Last Element: 3
Explanation 1
The array is not sorted, and its initial values are: . The following  swaps take place:

At this point the array is sorted and the three lines of output are printed to stdout."""


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




