"""
leetcode # 2164

Given an array of integers, we should rearrange the values of the array
according the following rules:

* sort values in odd indices in decreasing order
* sort values in even indices in increasing order

We then return the array formed after rearranging values.
"""

import itertools


def rearrange_odd_even(arr):
    """
    We split the input list into two lists of numbers present in odd or even
    indices, then we sort them according to the challenge rules. We then
    assemble these two lists.

    Time complexity: O(nlog(n)) because of sorting.

    :param list arr: Array of integers.
    :returns (list): Sorted array.
    """
    even = []
    odd = []
    for i, n in enumerate(arr):
        if i & 1:
            odd.append(n)
        else:
            even.append(n)
    odd.sort(reverse=True)
    even.sort()
    return [i for tup in itertools.zip_longest(even, odd) for i in tup if i]
