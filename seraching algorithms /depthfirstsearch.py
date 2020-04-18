from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, v, e):
        self.graph[v].append(e)

    def depth_first_search(self, v):
        visited = []

        return self.depth_first_search_recursive(v, visited)

    def depth_first_search_recursive(self, v, visited):
        # mark current vertex as visited
        visited.append(v)

        for node in self.graph[v]:
            if node not in visited:
                self.depth_first_search_recursive(node, visited)

