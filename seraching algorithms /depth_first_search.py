from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)
        self.graph[edge].append(vertex)

    def depth_first_search(self, target_vertex):
        visited = []
        current_vertex = 0

        return self.depth_first_search_helper(current_vertex, target_vertex, visited)

    def depth_first_search_helper(self, current_vertex, target_vertex, visited):
        if current_vertex == target_vertex:
            return True

        visited.append(current_vertex)

        for vertex in self.graph[current_vertex]:
            if vertex not in visited:
                return self.depth_first_search_helper(vertex, target_vertex, visited)

        return False

"""

0 --- 1 --- 2 
|     |     |
|     |     |
5     4 --- 3

call: depth_first_search(3)  



"""

if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 5)
    g.add_edge(1, 4)
    g.add_edge(1, 2)
    g.add_edge(4, 3)
    g.add_edge(2, 3)
    print(g.depth_first_search(3))
"""
depth_first_search(3)  
visited = [0, 5, 1, 2]
current_vertex = 3


0 --- 1 --- 2 
|     |     |
|     |     |
5     4 --- 3


"""
