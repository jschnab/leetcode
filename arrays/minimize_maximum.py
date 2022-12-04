"""
leetcode 2439: minimize maximum of array

We are given an integer array A comprising n non-negative integers.

In one operation, we must:

* choose an integer i such that 1 <= i < n and A[i] > 0
* decrease A[i] by 1
* increase A[i - 1] by 1

Return the minimum possible value of the maximum integer of A after performing
any number of operations.
"""
import itertools
import math


def min_max(A):
    """
    We reduce A[i] to the (integer) average of the elements of A between A[0]
    and A[i] (inclusive).
    """
    return max(
        math.ceil(n / i)
        for i, n in enumerate(itertools.accumulate(A), start=1)
    )


def test1():
    assert min_max([3, 7, 1, 6]) == 5
    print("test 1 successful")


def test2():
    assert min_max([10, 1]) == 10
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
