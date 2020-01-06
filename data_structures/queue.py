'''
A queue is a FIFO linear data structure that supports constant time insertion and deletion.
It's implemented by the use of a linked list normally due to the fact that we need O(1) insert and delete.

When we pop the first element from a dynamic array this is a O(N) complexity operation as we need to
shift the data stored in memory to fix the indexing.

The queue will be implemented as a Singly Linked List
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        '''
        Adds a node containing data to the end of the queue

        If there is a tail we update the pointers
        If the queue is empty then also update the head

        :param data: the data to be inserted into FIFO queue
        :return:
        '''

        # if queue is empty
        node = Node(data)
        if self.tail:
            self.tail.next = node

        self.tail = node

        if not self.head:
            self.head = node

    def dequeue(self):
        '''
        Pops the element first in line
        :return: removes the first node in line and returns the data
        '''
        pass

    def empty(self):
        '''

        :return: True if queue is empty else False
        '''

        return self.head == None

    def peek(self):
        '''

        :return: the data stored in the node first in line
        '''