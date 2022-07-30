"""
leetcode 2294: partition array such that maximum difference is k

We are given an integer array A and an integer k. We can partition A into one
or more subsequences such that each element of A appears in exactly one of the
subsequences.

Return the minimum number of subsequences needed such that the difference
between the maximum and minimum values in each subsequence is at most k.

A subsequence is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of remaining elements.
"""


def partition(A, k):
    A.sort()
    result = 1
    i = 0
    for j in range(len(A)):
        if A[j] - A[i] > k:
            result += 1
            i = j
    return result


def test1():
    assert partition([3, 6, 1, 2, 5], 2) == 2
    print("test 1 successful")


def test2():
    assert partition([1, 2, 3], 1) == 2
    print("test 2 successful")


def test3():
    assert partition([2, 2, 4, 5], 0) == 3
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
