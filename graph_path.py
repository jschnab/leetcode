# calculates the number of paths going from top-left to bottom-right in a 2D matrix
# while avoiding boulders
# 1|1|0
# 0|1|1
# 0|1|1
# two paths are valid for the previous matrix so the answer is 2

def path(grid):
    """Number of paths from top-left to bottom right while avoiding boulders."""
    
    m = len(grid)
    n = len(grid[0])
    
    # we will fill an image of the original grid with possible paths
    # which will sum up to the number of paths
    paths = [[0] * n for _ in range(m)]
    paths[0][0] = 1

    # initialize first row
    for j in range(1, n):
        if grid[0][j]:
            paths[0][j] = grid[0][j-1]

    # initialize first column
    for i in range(1, m):
        if grid[i][0]:
            paths[i][0] = grid[i-1][0]
    
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j]:
                paths[i][j] =  paths[i-1][j] + paths[i][j-1]

    print(paths)
    return paths[m-1][n-1]

if __name__ == '__main__':
    grid = [[1,1,0],[0,1,1],[1,1,1]]
    print(path(grid))
    grid = [[1,1,1],[1,1,1],[0,1,1],[0,0,1]]
    print(path(grid))
