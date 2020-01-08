'''
Binary search performs searching in a sorted array and runs in O(log N) time and O(log N) space
when implemented recursively due to the memory usage in the call stack.

It works by comparing the value to search for to the mid point.

    1) if value == mid then return True
    2) if value > mid then search in the r.h.s (mid + 1 to right) of the array
    3) if value < mid then search in the l.h.s (left to mid - 1) of the array
    4) when left > right i.e. right is out of bounds when searching r.h.s and negative when searching l.h.s
        return False

Since we are eliminating half of the array on every call to the function the time complexity is O(log N)
'''

def binary_search(array, value):
    return binary_search_recursive(array, value, 0, len(array) - 1)

def binary_search_recursive(array, value, left, right):

    # base case
    if left > right:
        return False

    # floor division
    mid = (left + right) // 2

    # check if we have found the value
    if value == array[mid]:
        return True

    elif value < array[mid]:
        # search the l.h.s of the array
        return binary_search_recursive(array, value, left, mid - 1)
    else:
        return binary_search_recursive(array, value, mid + 1, right)

if __name__ == '__main__':
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]

    assert True == binary_search(array, 61)
    assert False == binary_search(array, -1)
