# leetcode challenge 64

# a recursion depth-first search approach is very long
# a dynamic-programming approach is not too difficult

def minPathSum(grid):
    """
    Get the minimum sum of values along the path from top left
    to bottom right of a grid. Allowed movements are only step right
    of step down.
    """

    m = len(grid)
    n = len(grid[0])

    memo = [[0] * n for _ in range(m)]

    # initialize memo
    memo[0][0] = grid[0][0]

    # initialize first row
    for j in range(1, n):
        memo[0][j] = memo[0][j-1] + grid[0][j]

    # initialize first column
    for i in range(1, m):
        memo[i][0] = memo[i-1][0] + grid[i][0]

    # fill rest of the memo by performing path
    for i in range(1, m):
        for j in range(1, n):
            if memo[i-1][j] > memo[i][j-1]:
                memo[i][j] = memo[i][j-1] + grid[i][j]
            else:
                memo[i][j] = memo[i-1][j] + grid[i][j]

    return memo[m-1][n-1]

if __name__ == '__main__':
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print('minPathSum should return 7')
    print(minPathSum(grid))
