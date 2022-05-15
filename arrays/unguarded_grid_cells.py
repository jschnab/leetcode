"""
leetcode 2257: count unguarded cells in grid

Given two integers m and n representing an m x n grid, two 2D integer arrays G
and W where G[i] = [x_i, y_i] and W[j] = [x_j, y_j], representing the position
of guards and walls in the m x n grid.

A guard can see every cell in the four cardinal directions (up, down, left,
right), starting from their position, unless obstructed by a wall or another
guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.
"""

# use digits to have a nicer print of the grid
# 6 looks like G (for guard)
# 3 looks like W (for wall, if you rotate 90 deg clockwise)
GUARD = 6
WALL = 3


def count_unguarded(m, n, guards, walls):
    """
    We first build a grid filled with 0 and place guards and walls into it.
    Then we iterate through the grid and mark every cell that is guarded with a
    1. The solution is the number of 0 left in the grid.

    To determine if a cell is guarded, we iterate through cells in a row and
    then in a column, and determine if a guard was encountered on the linear
    path to each cell. We iterate in two directions (left then right for rows
    and down then up for columns) because a guard can see in all directions,
    but we iterate one direction at a time.
    """
    grid = [[0] * n for _ in range(m)]

    # place guards and walls on the grid
    for r, c in guards:
        grid[r][c] = GUARD
    for r, c in walls:
        grid[r][c] = WALL

    # mark cells that are guarded horizontally
    for i in range(m):
        # first go from left to right
        seen_guard = False
        for j in range(n):
            if grid[i][j] == GUARD:
                seen_guard = True
            elif grid[i][j] == WALL:
                seen_guard = False
            else:
                if seen_guard:
                    grid[i][j] = 1

        # then go from right to left
        seen_guard = False
        for j in reversed(range(n)):
            if grid[i][j] == GUARD:
                seen_guard = True
            elif grid[i][j] == WALL:
                seen_guard = False
            else:
                if seen_guard:
                    grid[i][j] = 1

    # mark cells that are guarded vertically
    for j in range(n):
        # first go from top to bottom
        seen_guard = False
        for i in range(m):
            if grid[i][j] == GUARD:
                seen_guard = True
            elif grid[i][j] == WALL:
                seen_guard = False
            else:
                if seen_guard:
                    grid[i][j] = 1

        # then go from bottom to top
        seen_guard = False
        for i in reversed(range(m)):
            if grid[i][j] == GUARD:
                seen_guard = True
            elif grid[i][j] == WALL:
                seen_guard = False
            else:
                if seen_guard:
                    grid[i][j] = 1

    # count unguarded cells
    # for row in grid:
    #    print(row)
    return sum(cell == 0 for row in grid for cell in row)


def test1():
    G = [[0, 0], [1, 1], [2, 3]]
    W = [[0, 1], [2, 2], [1, 4]]
    assert count_unguarded(4, 6, G, W) == 7
    print("test 1 successful")


def test2():
    G = [[1, 1]]
    W = [[0, 1], [1, 0], [2, 1], [1, 2]]
    assert count_unguarded(3, 3, G, W) == 4
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
