X = [-1, 0, 0, 1]
Y = [0, -1, 1, 0]
def find_path_util(matrix, path, i, j, m, n):
    if [i, j] == [m - 1, n - 1]:
        return True
    for k in range(4):
        x, y = i + X[k], j + Y[k]
        if 0 <= x < m and 0 <= y < n and matrix[x][y] == 1:
            path[x][y] = 1
            matrix[x][y] = 0
            if find_path_util(matrix, path, x, y, m, n):
                matrix[x][y] = 1
                return True
            matrix[x][y] = 1
            path[x][y] = 0

def find_path(matrix):
    m, n = len(matrix), len(matrix[0])
    path = [[0 for _ in range(n)] for _ in range(n)]
    find_path_util(matrix, path, 0, 0, m, n)
    path[0][0] = 1
    return path

if __name__=='__main__':
#     Inputs
#     Test Case: 1
    # matrix = [[0, 0, 0, 1, 0],
    #           [1, 0, 0, 1, 1],
    #           [0, 0, 0, 1, 0],
    #           [1, 0, 1, 0, 1],
    #           [0, 0, 1, 0, 0]]
    
#     Test Case: 2
    matrix = [[1, 0, 0, 0, 0],
              [1, 0, 1, 1, 1],
              [1, 1, 1, 0, 1],
              [1, 0, 0, 0, 1],
              [1, 0, 0, 0, 1]]
    path = find_path(matrix)
    for p in path:  print(p) 
    print()    
    for p in matrix:  print(p)