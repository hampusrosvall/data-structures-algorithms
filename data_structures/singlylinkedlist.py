'''
Implementation of a SinglyLinkedList - basically a sequence of linked elements (nodes)
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
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        '''
        O(1) append operation to the end of the list due to the reference to the tail

        Edge cases:
        1) list is empty
        2) list contains one element
        3) list contains > one element

        :param data: the data to be stored in the new node
        :return:
        '''

        # case: list is empty
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = self.head

        # case: list has one element
        elif not self.head.next:
              self.head.next = node
              self.tail = node
        # case: list has > one element
        else:
            self.tail.next = node
            self.tail = node

    def prepend(self, data):
        '''
        O(1) prepend operation to the beginning of the list

        Edge cases:
        1) list is empty
        2) list contains one element
        3) list contains > one element

        :param data: the data to be stored in the new node
        :return:
        '''

        # case: list is empty
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = self.head

        # case: list has one element
        elif not self.head.next:
            node.next = self.head
            self.tail = self.head
            self.head = node
        # case: list has > one element
        else:
            node.next = self.head
            self.head = node


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
            return
        else:
            # start iteration at head
            node = self.head
            # traverse as long as we have a following node
            while node.next:
                if node.next.data == data and node.next is not self.tail:
                    node.next = node.next.next
                    return

                if node.next.data == data and node.next is self.tail:
                    node.next = None
                    self.tail = node
                    return

                node = node.next






if __name__ == '__main__':
    # test append method
    singly_linked_list = SinglyLinkedList()

    for val in range(10):
        singly_linked_list.append(val)

    arr = []
    node = singly_linked_list.head

    while node:
        arr.append(node.data)
        node = node.next
    print('Append test')
    print(arr)

    # test append method
    singly_linked_list = SinglyLinkedList()

    for val in range(10):
        singly_linked_list.prepend(val)

    arr = []
    node = singly_linked_list.head

    while node:
        arr.append(node.data)
        node = node.next
    print('Prepend test')
    print(arr)

    # test delete with value
    singly_linked_list.delete_with_value(0)

    arr = []
    node = singly_linked_list.head

    while node:
        arr.append(node.data)
        node = node.next
    print('Prepend test')
    print(arr)



