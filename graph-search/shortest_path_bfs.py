from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, vertex, edge):
        # undirected graph property
        self.graph[vertex].append(edge)
        self.graph[edge].append(vertex)


    """
    q = [7, 6]
    parents = {0:None, 1:0, 3:0, 2:1, 4:3, 5:4, 7:4}
    (possibly unnecessary) visited = {0, 1, 3, 2, 4, 5, 7} --> break
    distance_from_source = {0:0, 1:1, 3:1, 2:2, 4:2, 5:3, 7:3}
    
    """
    def shortest_path(self, source, destination):
        # initialize queue to store vertices to explore
        queue = deque()

        # hash map that maps predecessor to a given vertex
        parents = {}
        distance = {}

        distance[source] = 0

        # add source to parents and queue
        parents[source] = None
        queue.append(source)

        while queue:
            # pop element from queue
            vertex = queue.pop()

            # check if we have reached the goal
            if vertex == destination:
                break
            for successor in self.graph[vertex]:
                if successor not in parents:
                    queue.append(successor)
                    parents[successor] = vertex
                    distance[successor] = distance[vertex] + 1

        path = [destination]
        predecessor = parents[destination]

        while predecessor is not None:
            path.insert(0, predecessor)
            predecessor = parents[predecessor]


        return distance[destination], path



if __name__ == '__main__':
    g = Graph()

    g.add_edge(0, 3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 4)
    g.add_edge(3, 7)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(7, 6)
    g.add_edge(6, 5)

    print(g.shortest_path(2, 6))
