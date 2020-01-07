'''
Binary search tree fulfills the following properties:
    1) given a root node of any BST the values of l.h.s < root value
    2) given a root node of any BST the values of r.h.s >= root value

Due to this we can implement O(log N) time complexity insertions, search and deletions

Implementing BST recursively makes insert, search and delete to operate in O(log N) space time aswell
due to the amount of calls stored in the call stack.

However, iterative implementation allows for O(1) space complexity.

Each node will have two pointers:
    - left, points to the node with value < root value
    - right, points to the node with value >= root value

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return

        if data < self.data:
            if not self.left:
                self.left = Node(data)
            else:
                # make sure to make the recusive call with respect to the left node
                self.left.insert(data)

        else:
            if not self.right:
                self.right = Node(data)
            else:
                # make sure to make the recursive call with respect to the right node
                self.right.insert(data)

    def get_values(self):
        '''
        traverse the tree in order i.e. left -> root -> right
        append the values to a list and return it
        O(N) space time operation
        :return:
        '''
        arr = []
        self.get_values_recursive(self.root, arr)
        return arr

    def get_values_recursive(self, root, array):
        if not root.left:
            array.append(root.data)
        else:
            self.get_values_recursive(root.left)
            array.append(root.data)
            self.get_values_recursive(root.right)



if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)


    print(bst.get_values())

