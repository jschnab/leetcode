"""
leetcode 2304: minimum path cost in a grid

We are given an m * n integer matrix G consisting of distinct integer from 0 to
m * n - 1. We can move in this matrix from a cell to any other cell in the next
row: if we are in cell (x, y) we can move to any of (x + 1, 0), (x + 1, 1),
..., (x + 1, n - 1). It is not possible to move from cells in the last row.

Each possible move has a cost given by a 2D array C of size (m * n) * n, where
C[i][j] is the cost of moving from a cell with value i to a cell in column j in
the next row. The cost of moving from cells in the last row of G can be
ignored.

The cost path in G is the sum of all values of cells visited plus the sum of
costs of all moves made. Return the minimum cost of a path that starts from any
cell in the first row and ends at any cell in the last row.
"""


def min_path_cost(G, C):
    tab = [[float("inf")] * len(G[0]) for _ in range(len(G))]
    tab[0] = G[0][::]

    for i in range(1, len(G)):
        for j in range(len(G[0])):
            for k in range(len(G[0])):
                tab[i][k] = min(
                    tab[i][k], tab[i - 1][j] + G[i][k] + C[G[i - 1][j]][k]
                )

    return min(tab[-1])


def test1():
    G = [[5, 3], [4, 0], [2, 1]]
    C = [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]
    assert min_path_cost(G, C) == 17
    print("test 1 successful")


def test2():
    G = [[5, 1, 2], [4, 0, 3]]
    C = [
        [12, 10, 15],
        [20, 23, 8],
        [21, 7, 1],
        [8, 1, 13],
        [9, 10, 25],
        [5, 3, 2],
    ]
    assert min_path_cost(G, C) == 6
    print("test 2 succesful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
