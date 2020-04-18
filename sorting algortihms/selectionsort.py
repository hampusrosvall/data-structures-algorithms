def selection_sort(array):
    for i in range(len(array)):
        smallest_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest_idx]:
                smallest_idx = j
        swap(i, smallest_idx, array)

    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

array = [8, 5, 2, 9, 5, 6, 3]

print(selection_sort(array))