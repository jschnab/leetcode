"""
leetcode 2317: maximum XOR after operations

We are given an integer array A. In one operation, we can select any
non-negative integer x and an index i, then update A[i] to be equal to
A[i] AND (A[i] XOR x).

Return the maximum possible bitwise XOR of all elements of A after applying the
operation any number of times.
"""

from functools import reduce


def max_xor(A):
    """
    When we XOR elements, the ideal case to maximize the result is to have the
    XOR operands to have different bits for each position.

    An operation can remove a bit but cannot add one, so the goal is to remove
    all bits shared between array elements.

    Therefore, the solution is to perform OR on all elements.

    :param list(int) A: Array to maximize.
    :returns (int): Result.
    """
    return reduce(lambda x, y: x | y, A)


def test1():
    assert max_xor([3, 2, 4, 6]) == 7
    print("test 1 successful")


def test2():
    assert max_xor([1, 2, 3, 9, 2]) == 11
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
