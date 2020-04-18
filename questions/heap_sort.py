"""
[8,5,2, 9, 5, 6, 3]

convert the array to a max heap and swap the largest element with the last index repeatedly

 0 1 2  3  4  5  6
[8,5,2, 9, 5, 6, 3]

parent_node = (children_node - 1) // 2
child_nodes = 2 * parent_node + 1 and 2

                     9
                   /   \
                  8     6
                 / \   / \
                5   5  2  3

[9, 8, 6, 5, 5, 2, 3] -> swap 9 with 3 and sift down three until the correct place

                     8
                   /   \
                  5     6
                 / \   /
                5   5  2

max-heap property: every parent is greater than (or equal to) its children
the maximum element in the heap is at the root in the binary tree
"""

def heap_sort(array):
    # convert input array to max heap
    parent_node = (len(array) - 1 - 1) // 2
    while parent_node >= 0:
        sift_down(array, parent_node, len(array) - 1)
        parent_node -= 1

    for swap_idx in reversed(range(len(array))):
        swap(array, 0, swap_idx)
        sift_down(array, 0, swap_idx - 1)

    return array

def sift_down(array, parent_idx, end_idx):
    c_one = 2 * parent_idx + 1 # 1st children index

    while c_one <= end_idx:
        c_two = c_one + 1 if c_one + 1 <= end_idx else None # 2nd children index

        if c_one and c_two:
            largest_idx = c_one if array[c_one] >= array[c_two] else c_two
            if array[parent_idx] < array[largest_idx]:
                swap(array, parent_idx, largest_idx)
                parent_idx = largest_idx
                c_one = 2 * parent_idx + 1
            else:
                break
        else:
            if array[parent_idx] < array[c_one]:
                swap(array, parent_idx, c_one)
                parent_idx = c_one
                c_one = 2 * parent_idx + 1
            else:
                break


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


array = [8,5,2, 9, 5, 6, 3]
print(heap_sort(array))