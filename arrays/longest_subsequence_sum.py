"""
leetcode 2389: longest subsequence with limited sum

We are given an integer array A of length n and an interger array Q (queries)
of length m.

Return an array (answer) of length m where answer[i] is the maximum size of a
subsequence that we can take from A such that the sum of its elements is less
than or equal to Q[i].

A subsequence is an array that can be derived from another array by deleting
some or no elements without changing the order of the remaining elements.
"""
import itertools


def bin_search(A, x, left=0, right=None):
    """
    Return the index of the leftmost element of A that is smaller than x. In
    other words, return i such that all elements of A[:i] are smaller than or
    equal to x and all elements of A[i:] are greater than x.

    If x already appears in A, A.insert(i, x) will insert just after the
    rightmost x in A.

    This is equivalent to bisect.bisect_right() from standard library.

    :param list(int) A: Array.
    :param int x: Target value.
    :param int left: Left index for search.
    :param int right: Right index for search.
    :returns (int): Index of insertion site.
    """
    right = right or len(A)
    while left < right:
        mid = (left + right) // 2
        if x < A[mid]:
            right = mid
        else:
            left = mid + 1
    return left


def answer(A, Q):
    prefix_sum = list(itertools.accumulate(sorted(A)))
    return [bin_search(prefix_sum, q) for q in Q]


def test1():
    assert answer([4, 5, 2, 1], [3, 10, 21]) == [2, 3, 4]
    print("test 1 successful")


def test2():
    assert answer([2, 3, 4, 5], [1]) == [0]
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
