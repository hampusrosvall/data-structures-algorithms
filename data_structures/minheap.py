class MinHeap:
    def __init__(self, array):
        self.heap = self.build_heap(array)

    def build_heap(self, array):
        arr_len = len(array) - 1
        parent_idx = (arr_len - 1) // 2

        for i in reversed(range(parent_idx + 1)):
            self.bubble_down(i, array)

        return array

    def bubble_up(self):
        heap_len = len(self.heap) - 1
        parent_idx = (heap_len - 1) // 2
        elem_idx = heap_len

        while parent_idx >= 0:
            if self.heap[elem_idx] < self.heap[parent_idx]:
                self.swap(elem_idx, parent_idx)
                elem_idx = parent_idx
                parent_idx = (parent_idx - 1) // 2
            else:
                break

    def bubble_down(self, start_idx, heap):
        end_idx = len(heap) - 1
        parent_idx = start_idx
        child_one = 2 * parent_idx + 1

        while child_one <= end_idx:
            child_two = child_one + 1 if child_one + 1 <= end_idx else None

            if child_one and child_two:
                smallest_idx = child_one if heap[child_one] < heap[child_two] else child_two
                if heap[smallest_idx] < heap[parent_idx]:
                    self.swap(smallest_idx, parent_idx, heap)
                    parent_idx = smallest_idx
                else:
                    break
            else:
                if heap[parent_idx] < heap[child_one]:
                    self.swap(parent_idx, child_one, heap)
                    parent_idx = child_one
                else:
                    break 

            child_one = 2 * parent_idx + 1


    def insert(self, value):
        self.heap.append(value)
        self.bubble_up()

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        val = self.heap.pop(-1)

        start_idx = 0
        self.bubble_down(start_idx)

        return val

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

if __name__ == '__main__':
    array = [19, 18, 15, 12, 9]
    heap = MinHeap(array)
    print(heap.heap)
