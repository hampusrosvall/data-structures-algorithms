'''
The iterative implementation of BST is advantageous in the sense that:

    1) insert, delete, search still runs in O(log N) time complexity
    2) insert, delete, search runs in O(1) space as we don't store calls in the function call stack

The statements above are based on a balanced tree.
The worst case is O(N) time and O(1) space

'''

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self

        while True:
            if value < self.value:
                if not self.left:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = self.left

            else:
                if not self.right:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right

    def contains(self, value):
        currentNode = self

        while currentNode:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True

        return False


    def remove(self, value, parentNode = None):
        '''

        :param value: the value to be deleted
        :param parentNode: pointer to the parent node

        Deletion is pretty complicated. We have a few subcases we need to take care of.

        Traverse to the node that is to be deleted.

        Check:

            1) if the node has two children then we should find the smallest right most value and replace
                the node with that value. Then delete the smallest right most value

            2) now we kow that we have only one children node given the current node we're at.
                if the current node is root we can't reassign parent node pointers so we need to check this.

            3) if the node has only one children. check if it's a left or right child then point the
                parent node to the left node is possible else the right.

            4) if the node has none children then check if it's a left or right node and change the pointer
                of the parent node
        :return:
        '''
        # find the value that we try to remove
        currentNode = self

        while currentNode:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left

            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right

             # we have found our node
            else:
                # subcase: node has two children nodes
                if currentNode.left and currentNode.right:
                    # set the currentNode.value to be the smallest value in r.h.s subtree
                    currentNode.value = currentNode.right.getMinValue()

                    # remove that very value from the r.h.s subtree
                    currentNode.right.remove(currentNode.value, currentNode)
                # we're at a node that doesn't point to two children

                # special case for the root as we don't have a parent node
                elif not parentNode:
                    if currentNode.left:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left

                    elif currentNode.right:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    # we delete the tree basically
                    else:
                        currentNode.value = None
                # subcase: the node is a left node
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left else currentNode.right

                # subcase: the node is a right node
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left else currentNode.right

                break


    def getMinValue(self):
        if not self.left:
            return self.value
        else:
            return self.left.getMinValue()

