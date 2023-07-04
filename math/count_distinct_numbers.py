"""
leetcode 2549: count distinct numbers on board

We are given a positive integer n, that is initially placed on a board. Every
day, for 1 billion days, we perform the following procedure:

    1. For each number x present on the board, we find all numbers i such that
       1 <= i <= n and x % i == 1.
    2. We place each number x on the board.

Return the number of distinct integers present on the board after 1 billion
days have elapsed.
"""


def count_numbers(n):
    """
    Assuming that n < 1 billion, at least n - 1 satisfies the problem
    conditions. Then, all numbers between 1 and n - 1 (inclusive) will
    eventually be on the board.
    """
    return n - 1


def test1():
    assert count_numbers(3) == 2
    print("test 1 successful")


def test2():
    assert count_numbers(5) == 4
    print("test 2 successful")


if __name__ == "__main__":
    test1()
    test2()
