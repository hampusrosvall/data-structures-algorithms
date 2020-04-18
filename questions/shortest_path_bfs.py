"""
Given an undirected, cyclic graph.
Find shortest path from node A -> B

traverse graph in breadth first manner

1) keep track of steps w.r.t the starting node at each node
    - implemented using a hash-map that maps {node : distance} w.r.t the starting node

0 ---- 1 ----- 2
|      |       |
|      |       |
5      4 ----- 3

                0 -- 1
              /  \
             N .. 2  need to store V + E elements in list
shortest_path(0, 3)

visited = [0, 5, 1, 2, 4, 3]
queue = []
distance {0:0, 5:1, 1:1, 2:2, 4:2, 3:3}

return distance[target] -> shortest distance

runtime: O(V + E)
space: O(V)


"""
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)
        self.graph[edge].append(vertex)

    def shortest_path(self, start, target):
        visited = list()
        distances = dict()

        # use list to represent FIFO queue with O(1) insertion and deletion at start and end of list
        queue = list()

        queue.append(start)
        distances[start] = 0
        while queue:
            current_vertex = queue.pop(0)
            visited.append(current_vertex)

            if current_vertex == target:
                break

            for v in self.graph[current_vertex]:
                if v not in visited:
                    queue.append(v)
                    distances[v] = distances[current_vertex] + 1
        return distances[target] if target in distances else -1

if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 5)
    graph.add_edge(1, 4)
    graph.add_edge(1, 2)
    graph.add_edge(4, 3)
    graph.add_edge(2, 3)

    print(graph.shortest_path(1, 1))








