def quick_sort(array):
    return quick_sort_recursive(array, 0, len(array) - 1)

def quick_sort_recursive(array, start_index, end_index):
    # validate input index
    if start_index >= end_index:
        return

    # initialize pointers to indices in array
    pivot, left, right = start_index, start_index + 1, end_index

    while left <= right:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            swap(left, right, array)
        elif array[left] <= array[pivot]:
            left += 1
        else:
            right -= 1

    swap(pivot, right, array)

    quick_sort_recursive(array, start_index, right - 1)
    quick_sort_recursive(array, right + 1, end_index)

    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

array = [8, 5, 2, 9, 5, 6, 3]
array_c = ['e', 'f', 'g', 'a', 'z', 'w']

print(quick_sort(array_c))
print(quick_sort(array))