"""
leetcode 862: shortest subarray with sum at least k

Given an integer array A and an integer k, return the length of the shortest
non-empty subarray of A with a sum at least k. If there is no such subarray,
return -1.

Elements of A belong to the set of integers (negative, 0, positive).

A subarray is a contiguous part of an array.


Explanations
------------

A brute-force solution would calculate all subarray sums and identify which
subarray(s) has (have) the shortest length.

We do not need to calculate all subarray sums from scratch. An array of prefix
sums and appropriate subtractions on prefix sums allow us to compare subarrays.
Consider the following array A, and its prefix sums B:

index: 0 1  2 3 4
A:     1 3 -1 2 2
B:     1 4  3 5 7

The sum of the subarray between index i (inclusive) and j (exclusive) is:
sum(A[i:j]) = B[j - 1] - B[i - 1]

A solution with O(n^2) time complexity and O(n) space complexity would
calculate the prefix sums of the whole input array, then iterate over all pairs
of array indices to find the solution.

We can improve this solution by ignoring some indices once they provided a
solution:

1. As index j increases, we can remove i indices that provided a
   solution because they would only contribute to longer subarray lengths.

2. We can ignore subarrays starting at negative elements, because they lead to
   longer solution. We don't need to wait to have a solution to ignore these
   subarrays, we can remove prefix sums as we build B.

One subtlety to accommodate these two improvements is that we can to remove
prefix sums in different parts of array B. In (1) we remove indices from the
left (when we calculate subarray sums) and in (2) we remove elements from the
right (when we calculate prefix sums). This can be achieved efficiently by
using a double-ended queue, which allows adding and removing elements from
either end in constant time.

For this problem, Kadane's algorithm (determine maximum sum of any subarray)
does not work because of negative integers. Kadane would find a solution that
encompasses them while the actual solution could be on one side or the other of
some negative integers.
"""

import sys
from collections import deque


def shortest_subarray(A, k):
    result = sys.maxint
    sum_ = 0  # prefix sum
    q = deque([(-1, 0)])

    for idx, value in enumerate(A):
        sum_ += value

        # Once a solution is found, keeping items in q only leads to longer
        # subarrays.
        while len(q) > 0 and sum_ - q[0][1] >= k:
            result = min(result, idx - q.popleft()[0])

        # Ignore subarrays that start at negative elements.
        while len(q) > 0 and sum_ <= q[-1][1]:
            q.pop()

        q.append((idx, sum_))

    if result < sys.maxint:
        return result

    return -1
