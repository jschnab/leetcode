# leetcode 26 (easy)

# given a list of sorted integers, remove duplicates in place
# and return the length of the list without duplicates

# example: given [0, 1, 1, 1, 2, 2]
# modify the list to [0, 1, 2, 1, 2, 2] and return 3

from random import choice


def remove_duplicates(nums):
    """
    Remove duplicates from integer list in place, using two pointers
    i (slow) and j (fast).

    Time complexity: O(n)
    Space complexity: O(1)

    :param list[int] nums: list of sorted integers
    :return int: length of the list without duplicates
    """
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1


if __name__ == "__main__":
    nums = [choice([0, 1, 2, 3]) for _ in range(6)]
    nums.sort()
    print("Input list: ", nums)
    l = remove_duplicates(nums)
    print("Output list: ", nums[:l])
