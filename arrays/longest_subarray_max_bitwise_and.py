"""
leetcode 2419: longest subarray with maximum bitwise AND

We are given an integer array A of size n.

Consider a non-empty subarray from A that has the maimum possible bitwise AND.

Let k be the maximum value of the bitwise AND of any subarray of nums. Then,
only subarrays with a bitwise AND equal to k should be considered.

Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.
"""
import itertools


def longest(A):
    """
    We notice that the problem is equivalent to searching for the longest
    subarray of the maximum array value.
    """
    maxi = max(A)
    return max(len(list(g)) for k, g in itertools.groupby(A) if k == maxi)


def test1():
    assert longest([1, 2, 3, 3, 2, 2]) == 2
    print("test 1 successful")


def test2():
    assert longest([1, 2, 3, 4]) == 1
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
