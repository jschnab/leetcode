"""
A swap is defined as taking two distinct positions in the array
and exchanging the values in them.

A circular array has its first element follow the last.

Given a circular array containing zeros and ones, return the minimum
number of swaps to group all ones together.

Leetcode #2134.
"""

def min_swaps(nums):
    """
    We move a sliding window with size "number of ones" along the array
    and count the number of zeros in the window: this is the number of swaps
    we need to make. We keep track of the minimum number of swaps we find.

    :param list(int) nums: Array of 1s and 0s.
    :returns (int): Minimum number of swaps to group 1s together.
    """
    l = len(nums)
    n_ones = nums.count(1)
    mini = n_ones  # there cannot be more swaps that the number of ones
    window_sum = 0

    # we move a sliding window with size n_ones through the array
    # we increment each number and decrement numbers that fall out of the
    # window
    # indices go past the length of the array to account for the circularity
    for i in range(l + n_ones):
        window_sum += nums[i % l]  # index modulo length to wrap around end
        if i >= l:
            window_sum -= nums[i - s]
        mini = min(mini, s - n_ones)
    return mini
