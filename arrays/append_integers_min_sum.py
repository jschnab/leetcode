"""
leetcode 2195: Append k integers with minimal sum.

Given an integer array A and an integer k, we append to A k unique positive
integers that do not appear in nums such that the resulting total sum of the
appended integers is minimum. Determine the sum of the k integers that are
appended.
"""


def min_k_sum(A, k):
    """
    The minimal sum of k integers is the sum of the smallest possible integers.

    The brute force solution is to iterate incrementally through integers,
    starting at 1, and figure out wich integers are not already in A so that we
    can include them to calculat the sum.

    We can also use the fact that the sum of k successive integers is given by
    k * (k + 1) / 2, and use a de-duplicated and sorted A. We have then three
    cases:

    1. The greatest A item is smaller than k: We calculate the sum from 1 to
    k + len(A), and subtract the sum of A items.
    2. If the greatest A item is greater than k, we have two cases:
        2.a. If there are enough "free slots" to append k elements smaller than
        the greatest A item, we determine the index of the smallest item that
        has >= "free slots" on its left, we calculate the sum from 1 to
        k + i and subtract the sum of A elements up to A[i] (excluded).
        2.b. Otherwise we calculate the sum like in case 1.
    """
    sort = sorted(list(set(A)))

    # case 1
    if sort[-1] <= k:
        return (k + len(sort)) * (k + len(sort) + 1) // 2 - sum(sort)

    # determine the smallest item that has >= k free slots on its left
    for i, n in enumerate(sort):
        free = n - i - 1

        # case 2a
        if free >= k:
            return (k + i) * (k + i + 1) // 2 - sum(sort[:i])

    # case 2b
    return (k + len(sort)) * (k + len(sort) + 1) // 2 - sum(sort)
