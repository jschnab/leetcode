"""
leetcode 2248: Intersection of multiple arrays

Given a 2D array A where A[i] is an array of distinct integers, return the list
of integers that a present in each array of A, sorted in ascending order.
"""

from functools import reduce


def intersect(A):
    return sorted(list(reduce(lambda x, y: x & y, [set(i) for i in A])))


def test1():
    A = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
    assert intersect(A) == [3, 4]
    print("test 1 successful")


def test2():
    A = [[1, 2, 3], [4, 5, 6]]
    assert intersect(A) == []
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
