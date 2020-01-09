'''
Merge sort is a divide and counqour algorithm that runs a few steps:

    1) Given the input array of dimension N split it in two subarrays
    2) Call merge sort recursively on the two subarrays respectively until we reach arrays of length 1
    3) Sort and merge the results

The algorithm runs in O(N log N) time complexity due to the division into subarrays, hence we are
performing copies of O(N) time complexity and since we are dividing the subarrays into roughly half
on each call we make O(log N) calls - compare with binary search for instance.

The memory is O(N log N) aswell due to the copying of arrays
'''

def merge_sort(array):
    # base case:
    if len(array) == 1:
        return array

    # find middle point
    mid = len(array) // 2

    # the slicing doesn't include the mid for the left slice
    left = array[:mid]
    right = array[mid:]

    # define a helper method that merges the length of one arrays
    return merge_sorted_arrays(merge_sort(left), merge_sort(right))

def merge_sorted_arrays(left, right):
    sorted_array = [None] * (len(left) + len(right))
    k = i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array[k] = left[i]
            i += 1
        else:
            sorted_array[k] = right[j]
            j += 1

        k += 1

    # take care of case when we break out and we still have elements left in one list
    while i < len(left):
        sorted_array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        sorted_array[k] = right[j]
        j += 1
        k += 1

    return sorted_array

#array = [8, 5, 2, 9, 5, 6, 3]
array = [4, 3, 2, 1]

print(merge_sort(array))
