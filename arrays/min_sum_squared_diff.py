"""
leetcode 2333: minimum sum of squared difference

We are given two positive integer arrays 'nums1' and 'nums2', both of length n.

The of squared difference of arrays nums1 and nums2 is defined as the sum of
(nums1[i] - nums2[i])^2 for each 0 <= i < n.

We are also given two positive integers k1 and k2. We can modify any of the
elements of nums1 by +1 or -1 at most k1 times. Similarly for nums2 elements
and k2.

Return the minimum squared difference after modifying array nums1 at most k1
times and modifying array nums2 at most k2 times.

We are allowed to modify the array elements to become negative integers.
"""

import heapq


def min_sum(nums1, nums2, k1, k2):
    """
    """
    diff = [-abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
    heapq.heapify(diff)
    k = k1 + k2
    s = -sum(diff)
    if s < k:
        return 0
    while k > 0:
        maxi = -heapq.heappop(diff)
        gap = max(k // len(nums1), 1)
        if k < gap:
            k = 0
        else:
            k -= gap
            maxi -= gap
        heapq.heappush(diff, -maxi)
    return sum(i**2 for i in diff)


def test1():
    assert min_sum([1, 2, 3, 4], [2, 10, 20, 19], 0, 0) == 579
    print("test 1 successful")


def test2():
    assert min_sum([1, 4, 10, 12], [5, 8, 6, 9], 1, 1) == 43
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
