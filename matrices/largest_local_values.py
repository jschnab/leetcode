"""
We are given an n * n integer matrix M.

Generate an integer matrix N or size (n - 2) * (n - 2) such that:

* N[i][j] is equal to the largest value of the 3 * 3 matrix in M centered
around row i + 1 and column j + 1

In other words, we want to find the largest value in every contiguous 3 * 3
matrix in M.

Calculate and return N.
"""


def largest_local(M):
    n = len(M)
    N = [[None] * (n - 2) for _ in range(n - 2)]
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            N[i - 1][j - 1] = max(
                M[i - 1][j - 1],
                M[i - 1][j],
                M[i - 1][j + 1],
                M[i][j - 1],
                M[i][j],
                M[i][j + 1],
                M[i + 1][j - 1],
                M[i + 1][j],
                M[i + 1][j + 1],
            )
    return N


def test1():
    M = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    N = [
        [2, 2, 2],
        [2, 2, 2],
        [2, 2, 2],
    ]
    assert largest_local(M) == N
    print("test 1 successful")


def test2():
    M = [
        [9, 9, 8, 1],
        [5, 6, 2, 6],
        [8, 2, 6, 4],
        [6, 2, 2, 2]
    ]
    N = [[9, 9], [8, 6]]
    assert largest_local(M) == N
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
