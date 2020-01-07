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
        else:
            self.insert_recursively(data, self.root)

    def insert_recursively(self, data, root):
        if data < root.data:
            if not root.left:
                root.left = Node(data)
            else:
                self.insert_recursively(data, root.left)
        else:
            if not root.right:
                root.right = Node(data)
            else:
                self.insert_recursively(data, root.right)

    def contains(self, data):
        return self.contains_recursive(self.root, data)

    def contains_recursive(self, root, data):
        if root.data == data:
            return True
        elif data < root.data:
            if root.left:
                return self.contains_recursive(root.left, data)
        else:
            if root.right:
                return self.contains_recursive(root.right, data)

        return False

    def in_order_traversal(self):
        self.in_order_traversal_recursive(self.root)

    def in_order_traversal_recursive(self, root):
        if root:
            self.in_order_traversal_recursive(root.left)
            print(root.data)
            self.in_order_traversal_recursive(root.right)



if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(20)

    bst.in_order_traversal()

    print(bst.contains(20))
