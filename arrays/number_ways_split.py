"""
leetcode 2270

Given an integer array A of length n, A contains a valid split at index i if
the following are true:

- the sum of the first i + 1 elements is greater than or equal to the sum of
  the last n - i - 1 elements
- there is at least one element to the right of i (0 <= i N n - 1)
"""


def split_array(A):
    """
    Keep track of two sums and iterate through the array while adjusting the
    sums as you go.

    Time complexity: O(n).
    Space complexity: O(1).

    :param list(int) A: Array.
    :returns (int): Number of ways to split the array.
    """
    s1 = nums[0]
    s2 = sum(nums[1:])
    count = 0
    if s1 >= s2:
        count = 1
    for i in range(1, len(nums) - 1):
        s1 += nums[i]
        s2 -= nums[i]
        if s1 >= s2:
            count += 1
    return count
