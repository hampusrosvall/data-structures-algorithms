def bubble_sort(array):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                sorted = False

    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]



array = [8, 5, 2, 9, 5, 6, 3]

print(bubble_sort(array))