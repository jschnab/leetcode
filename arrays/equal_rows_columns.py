"""
leetcode 2352: equal row and column pairs

Given an n x n integer matrix M, return the number of pairs (r, c) such that
row r and column c are equal.

A row and column pairs is considered equal if they contain the same elements in
the same order.
"""

from collections import Counter


def equal_pairs(M):
    """
    """
    columns = Counter(zip(*M))
    return sum(columns[tuple(r)] for r in M)


def test1():
    M = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    assert equal_pairs(M) == 1
    print("test 1 successful")


def test2():
    M = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    assert equal_pairs(M) == 3
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
