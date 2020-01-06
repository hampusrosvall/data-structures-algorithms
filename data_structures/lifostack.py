'''

The built in dynamic Python list has the desired properties of the stack data structure i.e.
Support constant time insertion, O(1), and deletion at the end of the array.

However, it's still possible to implement a stack as a LIFO queue

As for the queue a traversal operation stills runs in linear, O(N), time.

This implementation will be based on a singly linked list.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LIFOstack:
    def __init__(self):
        self.head = None
        self.tail = None

    def pop(self):
        '''
        Removes the element first in the stack
        :return: the data stored in the popped element
        '''

        if not self.empty():
            data = self.head.data
            self.head = self.head.next

            if not self.head:
                self.tail = None

            return data

        return None


    def push(self, data):
        '''
        Inserts a node containing the data in: data
        :param data: the data to be stored in the stack
        :return:
        '''
        node = Node(data)

        if self.head:
            node.next = self.head

        self.head = node

        if not self.tail:
            self.tail = node

    def peek(self):
        '''

        :return: the data stored in the first element in the stack
        '''

        return self.head.data

    def empty(self):
        '''
        Checks whether the stack is empty
        :return: True if the stack is empty else False
        '''

        return self.head == None


if __name__ == '__main__':
    q = LIFOstack()

    for val in range(10):
        q.push(val)

    arr = []
    data = q.pop()
    while data is not None:
        arr.append(data)
        data = q.pop()

    print(arr)