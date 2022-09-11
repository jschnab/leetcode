"""
leetcode 2369: check if there is a valid partition for the array

We are given an integer array A. We have to partition the array into one or
more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays
satisfies one of the following conditions:

1. the subarray consists of exactly 2 equal elements
2. the subarray consists of exactly 3 equal elements
3. the subarray consists of exactly 3 consecutive increasing elements (i.e. the
difference between the elements is 1)

Return true if the array has at least one valid partition. Otherwise, return
false.
"""
from functools import lru_cache


def check(A, i, j, memo):
    """
    Recursively determine if the array has a valid partition, using memoization
    to avoid re-computing previously seen results.

    We recurse through the array, trying to find invalid partitions.

    :param list(int) A: Array.
    :param int i: Start index of the partition (inclusive).
    :param int j: End index of the partition (exclusive).
    :param dict memo: Result cache for memoization.
    :returns (bool): True if the array has at least a valid partition, else
        False.
    """
    if (i, j) in memo:
        return memo[(i, j)]

    # We finished iterating through the array, so the array must have at least
    # one valid partition.
    if i == len(A):
        return True

    # The current partition is invalid, because its end is out of bounds.
    if j > len(A):
        return False

    # Check condition 1.
    if j - i == 2:
        if A[i] != A[i + 1]:
            return False

    elif j - i == 3:
        # Check conditions 2 and 3.
        if any([A[i] != A[i + 1], A[i + 1] != A[i + 2]]) and any(
            [A[i] + 1 != A[i + 1], A[i + 1] != A[i + 2] - 1]
        ):
            return False

    memo[(j, j + 2)] = check(A, j, j + 2, memo)
    memo[(j, j + 3)] = check(A, j, j + 3, memo)
    return memo[(j, j + 2)] or memo[(j, j + 3)]


def valid2(A):
    @lru_cache()
    def dfs(i):
        if i >= len(A) - 1:
            return i == len(A)
        two = i < len(A) - 1 and A[i] == A[i + 1]
        three = i < len(A) - 2 and (
            (two and A[i + 1] == A[i + 2])
            or (A[i] + 1 == A[i + 1] and A[i] + 2 == A[i + 2])
        )
        return (two and dfs(i + 2) or (three and dfs(i + 3)))

    return dfs(0)


def valid(A):
    memo = {}
    return check(A, 0, 2, memo) or check(A, 0, 3, memo)


def test1():
    assert valid([4, 4, 4, 5, 6]) is True
    assert valid2([4, 4, 4, 5, 6]) is True
    print("test 1 successful")


def test2():
    assert valid([1, 1, 1, 2]) is False
    assert valid2([1, 1, 1, 2]) is False
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
