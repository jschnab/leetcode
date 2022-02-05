"""
Leetcode challenge #2146

We are given an m * n 2D array containing positive integers that represent
items in a shop:

* 0 represents a wall we cannot go through
* 1 represents an aisle that we can walk through
* any other integer represents the value of an item (we can move through
    items like they are an aisle)

It takes 1 step to travel vertically or horizontally between grid cells.

We are given minimum and maximum item values that indicate which inclusive
value range we are interested in.

We are given starting coordinates from where we move through the shop and
look for items.

We are given an integer k.

We need to return the k highest-ranked items within the given price range,
as a list of tuples (row, column) representing item coordinates.

The rank is determined by the following criteria, in decreasing order of
importance (lower criteria are used to rank ties):

* distance from the start
* value
* row index
* column index
"""

from collections import deque


def k_ranked_items(grid, price_low, price_high, start_row, start_col, k):
    """
    Determine the k highest-ranked items.

    :param list[list[int]] grid: Items grid.
    :param int price_low: Low boundary for price range.
    :param int price_high: High boundary for price range.
    :param int start_row: Starting row.
    :param int start_col: Starting column.
    :param int k: Number of items to return.
    """
    m = len(grid)
    n = len(grid[0])

    # keep a queue for breadth-first search
    q = deque()

    # each queue item is a tuple (distance, value, row, column)
    initial = (0, grid[start_row][start_col], start_row, start_col)
    q.appendleft(initial)

    # keep track of visited grid cells
    seen = {(start_row, start_col)}

    # keep track of items within the price range
    items = []

    while q:
        dist, val, row, col = q.pop()
        if price_low <= val <= price_high:
            items.append((dist, val, row, col))

        # explore neighboring cells
        if (
            row - 1 >= 0
            and grid[row - 1][col] > 0
            and (row - 1, col) not in seen
        ):
            q.appendleft((dist + 1, grid[row - 1][col], row - 1, col))
            seen.add((row - 1, col))
        if (
            row + 1 < m
            and grid[row + 1][col] > 0
            and (row + 1, col) not in seen
        ):
            q.appendleft((dist + 1, grid[row + 1][col], row + 1, col))
            seen.add((row + 1, col))
        if (
            col - 1 >= 0
            and grid[row][col - 1] > 0
            and (row, col - 1) not in seen
        ):
            q.appendleft((dist + 1, grid[row][col - 1], row, col - 1))
            seen.add((row, col - 1))
        if (
            col + 1 < n
            and grid[row][col + 1] > 0
            and (row, col + 1) not in seen
        ):
            q.appendleft((dist + 1, grid[row][col + 1], row, col + 1))
            seen.add((row, col + 1))

    items.sort()
    return [(row, col) for _, _, row, col in items[:k]]


def test1():
    grid = [[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]]
    expected = [(0, 1), (1, 1), (2, 1)]
    actual = k_ranked_items(grid, 2, 5, 0, 0, 3)
    assert actual == expected
    print("test 1 successful")


def test2():
    grid = [[1, 2, 0, 1], [1, 3, 3, 1], [0, 2, 5, 1]]
    expected = [(2, 1), (1, 2)]
    actual = k_ranked_items(grid, 2, 3, 2, 3, 2)
    assert actual == expected
    print("test 2 successful")


def test3():
    grid = [[1, 1, 1], [0, 0, 1], [2, 3, 4]]
    expected = [(2, 1), (2, 0)]
    actual = k_ranked_items(grid, 2, 3, 0, 0, 3)
    assert actual == expected
    print("test 3 successful")


def test4():
    grid = [[1, 1, 1], [0, 0, 0], [2, 3, 4]]
    expected = []
    actual = k_ranked_items(grid, 2, 3, 0, 0, 3)
    assert actual == expected
    print("test 4 successful")


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
