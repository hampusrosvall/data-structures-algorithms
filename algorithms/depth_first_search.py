'''
Depth first search algorithm

Let V denote the # of vertices in the graph, let E denote the # of edges in the graph.
The time complexity for DFS is O(V + E) as each vertex has O(1) visit complexity
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

    def depthFirstSearch(self, array, visited_nodes):
        array.append(self.name)
        visited_nodes.add(self)
        for child in self.children:
            if child not in visited_nodes:
                child.depthFirstSearch(array, visited_nodes)

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
    visited_nodes = set()
    arr = node.depthFirstSearch(array, visited_nodes)
    print(arr)
    assert len(visited_nodes) == len(arr)


