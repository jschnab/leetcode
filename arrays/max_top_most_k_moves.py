"""
leetcode 2202: Maximize the topmost element after k moves

Given an integer array names 'nums' representing a pile, nums[0] is the topmost
element.

In one move, we can perform either of the following:

- if the pile is not empty, remove the topmost element
- if one or more elements have been removed, add an element back onto the pile

We are given an integer k, which denotes the total number of movement to make.

Return the maximum value of the topmost element of the pile possible after k
moves. In case the pile cannot be non-empty after k moves, return -1.
"""


def max_top(nums, k):
    """
    To visualize what elements are available to be on the top after k moves,
    we can make a table where columns are elements of the pile (top is left)
    and rows indicate how many moves we make. Each table enty indicates if
    an element can be on the top after k moves.

    We can see two things:
    - elements past index k cannot be on the top
    - the element at index k - 1 cannot be on the top (can only be removed
      but not added back)

    In conclusion we need to determine the pile element between the indices 0
    and k, excluding element at index k - 1.
    """
    if len(nums) == 1:
        if k & 1:
            return -1
        else:
            return nums[0]
    result = -1
    for index, value in enumerate(nums[:k+1]):
        if index == k - 1:
            continue
        result = max(result, value)
    return result


def test1():
    assert max_top([5, 2, 2, 4, 0, 6], 4) == 5
    print("test 1 successful")


def test2():
    assert max_top([2], 1) == -1
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
