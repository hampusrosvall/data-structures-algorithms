from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)
        self.graph[edge].append(vertex)

    def bfs_print(self, start_vertex):
        visited = []
        queue = []
        array = []
        queue.append(start_vertex)

        while queue:
            current_vertex = queue.pop(0)
            visited.append(current_vertex)
            array.append(current_vertex)

            for v in self.graph[current_vertex]:
                if v not in visited:
                    queue.append(v)
        return array

    def dfs_print(self, start_vertex):
        visited = []
        array = []
        return self.dfs_print_recursive(start_vertex, visited, array)

    def dfs_print_recursive(self, current_vertex, visited, array):
        array.append(current_vertex)
        visited.append(current_vertex)

        for v in self.graph[current_vertex]:
            if v not in visited:
                self.dfs_print_recursive(v, visited, array)

        return array

if __name__ == '__main__':
    """
       1 --- 2 --- 4
       |      \
       |       \
       0        3 --- 5

    """

    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)

    print(g.bfs_print(2))
    print(g.dfs_print(2))