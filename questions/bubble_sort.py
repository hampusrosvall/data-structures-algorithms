"""

[8,5,2,9,5,6,3]

iterate through array and swap elements if elem at index i + 1 is smaller than elem at index i

[2, 5, 5, 6, 3, 8, 9]
    |
"""
# time: worst/average O(N^2), best case O(N)
# space: O(1)
def bubble_sort(array):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(array) - 1):
            if array[i + 1] < array[i]:
                swap(array, i, i + 1)
                sorted = False
    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


array = "cba"

print(bubble_sort(array))
