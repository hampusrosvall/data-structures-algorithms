'''
Implementation of a Doubly Linked List - basically a sequence of linked elements (nodes)
Each node contains some data and also a pointer to the next node in the list (or None if there is none)

The advantage of Linked Lists as compared to arrays are:
Append to the end of the list is O(1) time operation (also for dynamic arrays)
Insertion at the beginning of the list is O(1) time operation (compared to O(N) for arrays - static or dynamic)

Typically we don't index the nodes as thus we don't have get/set methods - which would be O(N) due to traverse

Other common methods:
Initialize - O(N)
Copy - O(N)
Traverse - O(N)

I make use of two pointers, head and tail in order to support O(1) append

The main difference between a singly linked list and a doubly linked list is the pointer to the previous node
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        '''
        O(1) append operation to the end of the list due to the reference to the tail

        If there's a tail, update the pointer
        If not the tail will be set
        If the list is empty then set the head aswell

        :param data: the data to be stored in the new node
        :return:
        '''
        node = Node(data)

        if self.tail:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node

        if not self.head:
            self.head = node

    def prepend(self, data):
        '''
        O(1) prepend operation to the beginning of the list

        If the list is not empty then move the pointers
        Set the head of the list
        If we don't have a tail then point tail to the node

        :param data: the data to be stored in the new node
        :return:
        '''

        node = Node(data)
        if self.head:
            node.next = self.head
            self.head.prev = node

        self.head = node

        if not self.tail:
            self.tail = node


    def delete_with_value(self, data):
        '''
        O(N) deletion of nodes with value: data as traversal (O(N)) of data structure is required

        Assume unique values of each node

        Edge cases:
        1) List is empty
        2) List contains one element and the data is the value of the head
        3) List contains > one element and the data is the value of the head
        4) List contains > one element and the data is not the value of the tail
        5) List contains > one element and the data is the value of the tail

        For a singly linked list we need to perform the:
        while node.next statement since we then keep the reference to the current node
        this is required for moving the pointers around correctly when we encounter the node to delete

        :param data: the data to be deleted from the list
        :return:
        '''
        if not self.head:
            return
        elif self.head.data == data and not self.head.next:
            self.head = None
            self.tail = None
            return
        elif self.head.data == data and self.head.next:
            self.head = self.head.next
            self.head.prev = None
            return
        else:
            # start iteration at head
            node = self.head
            # traverse as long as we have a following node
            while node.next:
                if node.next.data == data and node.next is not self.tail:
                    node.next = node.next.next
                    node.next.prev = None
                    return

                if node.next.data == data and node.next is self.tail:
                    node.next = None
                    self.tail = node
                    return

                node = node.next

if __name__ == '__main__':
    # test append method
    doubly_linked_list = DoublyLinkedList()

    for val in range(10):
        doubly_linked_list.append(val)

    arr = []
    node = doubly_linked_list.head

    while node:
        arr.append(node.data)
        node = node.next
    print('Append test')
    print(arr)

    # test append method
    doubly_linked_list = DoublyLinkedList()

    for val in range(10):
        doubly_linked_list.prepend(val)

    arr = []
    node = doubly_linked_list.head

    while node:
        arr.append(node.data)
        node = node.next
    print('Prepend test')
    print(arr)

    # test delete with value
    doubly_linked_list.delete_with_value(5)

    arr = []
    node = doubly_linked_list.head

    while node:
        arr.append(node.data)
        node = node.next
    print('Prepend test')
    print(arr)



