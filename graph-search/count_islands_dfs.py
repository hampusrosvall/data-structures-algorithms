class Graph:
    def __init__(self, matrix):
        self.graph = matrix
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])
        self.visited = [[False for _ in range(self.n_cols)] for _ in range(self.n_rows)]

    def get_nbr_islands(self):
        nbr_islands = 0

        # for each pair (row, col) continue searching until we hit a zero or already visited node
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                # check if (row, col) is already visited and if the index is a one
                if not self.visited[row][col] and self.graph[row][col]:
                    self.DFS(row, col)
                    nbr_islands += 1

        return nbr_islands

    def DFS(self, row, col):
        # mark (row, col) as visited
        self.visited[row][col] = True

        inc_row = [0, 0, -1, 1]
        inc_col = [-1 , 1, 0, 0]
        for k in range(len(inc_row)):
            next_row = row + inc_row[k]
            next_col = col + inc_col[k]
            # check if it's a valid coordinate and if it's a one and not already visited
            if self.validate(next_row, next_col) and not self.visited[next_row][next_col] and self.graph[next_row][next_col]:
                self.DFS(next_row, next_col)

    def validate(self, row, col):
        return row >= 0 and row < self.n_rows and col >= 0 and col < self.n_cols

if __name__ == '__main__':
    matrix = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]

    graph = Graph(matrix)
    print(graph.get_nbr_islands())


