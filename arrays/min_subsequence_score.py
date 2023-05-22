"""
leetcode 2542: maximum subsequence score

We are given two integer arrays A and B of equal length n and a positive
integer k. We must choose a subsequence of indices from A of length k. For
chosen indices i(0), i(1), ..., i(k-1), the score is defined as the sum of the
selected elements from A multiplied by the minimum of the selected elements
from B.

Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from the
array by deleting some or no elements.
"""

import heapq


def max_score(A, B, k):
    """
    A brute force approach requires we check n!/(k!(n-k)! possibilities (we
    choose the unordered combination of k elements out of n), which quickly
    becomes a very large number.

    We note that if we sort B, we can determine the minimum of k elements of B
    with linear time complexity. Because we cannot change the relative order of
    elements in A and B, we sort pairs of (Ai, Bi) using Ai as a key. If we
    sort Ai,Bi pairs in decreasing order of Ai, once we choose Ai, we are free
    to choose k - 1 elements of B to the left (where Ai is greater that the
    current element).

    We can maximize the k - 1 elements of B by storing them in a a min-heap.
    Every time we add an element to the heap, we then pop an element and the
    heap will always store the maximum last k elements of B. The sum of the
    heap is multiplied with Ai to calculate the score.

    Sorting A is an n*log(n) operation. Pushing and popping from the heap is a
    log(k) operation, which is repeated k times then 2 * (n - k) times.
    Overall, the time complexity is O(n*log(n)).

    We store up to k items in a heap, so the space complexity is O(k).
    """
    pairs = sorted(zip(A, B), key=lambda x: x[1], reverse=True)
    q = []
    result = 0
    sum_top_k = 0
    for i in range(k):
        cur = pairs[i]
        sum_top_k += cur[0]
        heapq.heappush(q, cur[0])
    result = sum_top_k * cur[1]

    for i in range(k, len(pairs)):
        cur = pairs[i]
        sum_top_k += cur[0]
        heapq.heappush(q, cur[0])
        sum_top_k -= heapq.heappop(q)
        result = max(result, sum_top_k * cur[1])

    return result


def test1():
    assert max_score([1, 3, 3, 2], [2, 1, 3, 4], 3) == 12
    print("test 1 successful")


def test2():
    assert max_score([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1) == 30
    print("test 2 successful")


if __name__ == "__main__":
    test1()
    test2()
