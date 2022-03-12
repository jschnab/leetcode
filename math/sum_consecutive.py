"""
leetcode 2177: Find three consecutive integers that sum to a given number.

Given an integer N, return three consecutive integers (sorted) that sum to N.
If N cannot be expressed as the sum of three consecutive integers, return an
empty array.
"""


def consecutive(N):
    """
    If N is not a multiple of 3, we cannot express it as a sum of three
    numbers, so we return an empty array.

    Otherwise, the solution is N // 3, flanked by its neighbors.

    Time complexity: O(1).
    """
    if N % 3:
        return []
    else:
        return [N // 3 - 1, N // 3, N // 3 + 1]


def test1():
    assert consecutive(33) == [10, 11, 12]
    print("test 1 successful")


def test2():
    assert consecutive(32) == []
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
