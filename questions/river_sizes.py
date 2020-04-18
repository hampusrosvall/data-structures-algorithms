# runs in O(wh) time and O(wh) space 
def river_sizes(matrix):
    # get dimensions of input matrix
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    # initialize visited list to avoid redundant visits
    visited = list()
    river_sizes = list()

    for i in range(n_rows):
        for j in range(n_cols):
            if matrix[i][j] and (i, j) not in visited:
                queue = []
                queue.append((i, j))
                size = 0
                while queue:
                    # extract row and col
                    row, col = queue.pop(0)
                    size += 1

                    visited.append((row, col))

                    # check for adjacent ones
                    queue = append_adjacent_ones(row, col, matrix, visited, queue)

                river_sizes.append(size)



    return river_sizes

def append_adjacent_ones(row, col, matrix, visited, queue):
    inc_row = [-1, 1, 0, 0]
    inc_col = [0, 0, -1, 1]

    for k in range(len(inc_row)):
        n_r, n_c = row + inc_row[k], col + inc_col[k]
        if validate(n_c, n_r, len(matrix) - 1, len(matrix[0]) - 1):
            if matrix[n_r][n_c] and (n_r, n_c) not in visited:
                queue.append((n_r, n_c))

    return queue


def validate(row, col, n_rows, n_cols):
    return row >= 0 and row <= n_rows and col >= 0 and col <= n_cols

matrix = [
[1, 0, 0, 1, 0],
[1, 0, 1, 0, 0],
[0, 0, 1, 0, 1],
[1, 0, 1, 0, 1],
[1, 0, 1, 1, 0]
]

print(river_sizes(matrix))







