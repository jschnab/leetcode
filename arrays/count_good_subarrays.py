"""
leetcode 2537: count the number of good subarrays

Given an integer array nums and an integer k, return the number of good
subarrays of nums.

A subarray A is good if there are at least k pairs of indices (i, j) such that
i < j and A[i] == A[j].

A subarray is a contiguous non-empty sequence of elements within an array.
"""

import collections


def count(nums, k):
    """
    We count distinct array values over a window. The count allows us to
    calculate how many pairs of elements we have, which follows a triangular
    sequence (1, 3, 6, 10, 15, ...).

    When we find a subarray that has at least k pairs, we decrease the subarray
    size from the left until we have less than k pairs. At this point, the
    number of subarrays is the index of the left boundary of the subarray.

    Time complexity: O(n), we iterate at most twice (with two indices i and j)
    over the input array.
    Space complexity: O(n), we may store each array element in the counter
    dictionary.
    """
    result = 0
    count = collections.defaultdict(int)
    n_pairs = 0
    i = 0
    for j in range(len(nums)):
        count[nums[j]] += 1
        n_pairs += count[nums[j]] - 1
        while n_pairs >= k:
            count[nums[i]] -= 1
            n_pairs -= count[nums[i]]
            i += 1
        result += i
    return result


def test1():
    assert count([1, 1, 1, 1, 1], 10) == 1
    print("test 1 successful")


def test2():
    assert count([3, 1, 4, 3, 2, 2, 4], 2) == 4
    print("test 2 successful")


if __name__ == "__main__":
    test1()
    test2()
