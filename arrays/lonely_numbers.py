"""
Given an array of integers, we define a number as lonely if it appears only
once and has not adjacent number in the array (x + 1 and x - 1 do not appear
in the array).

Return the list of lonely numbers.
"""

from collections import Counter


def lonely(arr):
    """
    We use a dictionary to count each number in the array, then it's
    easy to determine if a number is unique and has neighbors.

    Time and space complexity are linear.

    :param list[int] arr: Array of integers.
    :returns (list[int]): List of lonely numbers.
    """
    count = Counter(arr)
    return [
        c for c in count if count[c] == 1 and count[c - 1] + count[c + 1] == 0
    ]


def test1():
    assert lonely([10, 6, 5, 8]) == [10, 8]
    print("test 1 successful")


def test2():
    assert lonely([1, 3, 5, 3]) == [1, 5]
    print("test 2 successful")


def test3():
    assert lonely([1, 1]) == []
    print("test 3 successful")


def test4():
    assert lonely([0]) == [0]
    print("test 4 successful")


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
