from collections import deque

class Graph:
    def __init__(self, matrix):
        self.graph = matrix
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])
        self.visited = [[False for _ in range(self.n_cols)] for _ in range(self.n_rows)]

    def get_nbr_islands(self):
        nbr_islands = 0
        queue = deque()
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                # search the graph in a breadth first manner
                if not self.visited[row][col] and self.graph[row][col]:
                    queue.append((row, col))
                    self.BFS(queue)
                    nbr_islands += 1

        return nbr_islands

    def BFS(self, queue):
        inc_row = [0, 0, -1, 1]
        inc_col = [-1, 1, 0, 0]

        while queue:
            row, col = queue.pop()
            self.visited[row][col] = True

            for k in range(len(inc_row)):
                nr, nc = row + inc_row[k], col + inc_col[k]
                valid = self.validate(nr, nc)
                if valid:
                    if not self.visited[nr][nc] and self.graph[nc][nr]:
                        queue.append((nr, nc))




    def validate(self, row, col):
        return row >= 0 and row < self.n_rows and col >= 0 and col < self.n_cols

if __name__ == '__main__':
    matrix = [
        [1, 1, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]

    graph = Graph(matrix)
    print(graph.get_nbr_islands())


