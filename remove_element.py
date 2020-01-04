# leetcode 27 (easy)
# the goal is to remove a given element in place from a list of integers
# and return the length of the resulting list
# the order of elements in the resulting list does not matter

# example: [3, 2, 2, 3] returns 2 and the list becomes [2, 2, ...]

from random import choice, randint


def remove_element(nums, val):
    """
    Remove elements having a certain value from a list of integers.
    Works in place by iterating through the list, swapping any element
    corresponding to the unwanted value with the last element and decreasing
    the length of the list by 1. This approach is used because the order of
    elements in the resulting list is not important.

    Time complexity: O(n)
    Space complexity: O(1)

    :param list[int] nums: list of integers to filter
    :param int val: value to remove from the list
    :return int: length of the resulting list
    """
    i = 0
    l = len(nums)
    while i < l:
        if nums[i] == val:
            nums[i] = nums[l - 1]
            l -= 1
        else:
            i += 1
    return l


def remove_element2(nums, val):
    """
    Remove elements having a certain value from a list of integers.
    Works in place by iterating through the list, with two pointers.
    This approach is inefficient if the element to remove is rare in the list
    but preserves the order of elements in the list.

    Time complexity: O(n)
    Space complexity: O(1)

    :param list[int] nums: list of integers to filter
    :param int val: value to remove from the list
    :return int: length of the resulting list
    """
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i


if __name__ == "__main__":
    nums = [randint(0, 10) for _ in range(5)]
    val = choice(nums)
    print("Input: ", nums)
    print("Value to remove: ", val)
    print("Output: ", nums[:remove_element2(nums, val)])
