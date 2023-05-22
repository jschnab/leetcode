"""
leetcode 2541: minimum operations to make array equal

We are given two integer arrays A and B of equal length n and an integer k. We
can perform the following operations on A: choose two indexes i and j and
increment A[i] by k and decrement A[j] by k.

A is said to be equal to B if for all indices i s.t. 0 <= i < n, A[i] == B[i].

Return the minimum number of operations required to make A equal to B. If it is
impossible, return -1.
"""


def min_op(A, B, k):
    """
    If it is possible to perform the described operation on A at index i, then
    the difference between A[i] and B[i] is a multiple of k. Also, after all
    such operations have been performed, the total number of decrements must
    match the total number of increments. Then the solution is the the number
    of decrements (or increments) divided by k. Otherwise, there is no
    solution.
    """
    if k == 0:
        if A == B:
            return 0
        return -1

    decrements = 0
    increments = 0
    for i in range(len(A)):
        if (A[i] - B[i]) % k != 0:
            return -1
        if A[i] < B[i]:
            increments += B[i] - A[i]
        elif A[i] > B[i]:
            decrements += A[i] - B[i]
    if decrements != increments:
        return -1
    return decrements // k


def test1():
    assert min_op([4, 3, 1, 4], [1, 3, 7, 1], 3) == 2
    print("test 1 successful")


def test2():
    assert min_op([3, 8, 5, 2], [2, 4, 1, 6], 1) == -1
    print("test 2 successful")


def test3():
    assert min_op([1, 2], [3, 4], 0) == -1
    print("test 3 successful")


def test4():
    assert min_op([1, 2], [1, 2], 0) == 0
    print("test 4 successful")


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
