'''
Breadth first search algorithm

Let V denote the # of vertices in the graph, let E denote the # of edges in the graph.
The time complexity for BFS is O(V + E) as each vertex has O(1) visit complexity
Each vertex has e edges where E denotes the total number of edges in the graph hence
For each vertex O(1) + O(e) --> O(V + E) in total

This algorithm takes in a directed graph and returns the values in the order of visit as an array
'''

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # initialize the queue as a dynamic array for simplicity
        # popping from any place except the end is O(N) operation in reality however

        queue = []
        queue.append(self)
        while queue:
            current_node = queue.pop(0)
            array.append(current_node.name)
            for children in current_node.children:
                queue.append(children)

        return array

if __name__ == '__main__':
    node = Node('A')

    # adding edges to A
    node.addChild('B')
    node.addChild('C')
    node.addChild('D')

    # adding edges to B
    node.children[0].addChild('E')
    node.children[0].addChild('F')

    # adding edges to F
    node.children[0].children[1].addChild('I')
    node.children[0].children[1].addChild('J')

    # adding edges to D
    node.children[2].addChild('G')
    node.children[2].addChild('H')

    # adding edges to G
    node.children[2].children[0].addChild('K')

    array = []
    arr = node.breadthFirstSearch(array)
    print(arr)