"""
leetcode #2149

Given an array of even length containing positive and negative integers
(excluding 0), we should produce an array where consecutive array items
have a different sign, the order of items with the same sign is preserved,
and the array starts with a positive integer.

There is the same number of positive and negative integers.
"""


def rearrange(arr):
    """
    We make two lists that contain either the positive or negative items
    in their original order, then we merge these lists into an array that
    satisfies the challenge constraints.

    Time and space complexity are linear.
    """
    pos = []
    neg = []
    for i in arr:
        if i > 0:
            pos.append(i)
        else:
            neg.append(i)
    return [i for tup in zip(pos, neg) for i in tup]


def test1():
    assert rearrange([-1, -2, -3, -4, 1, 2, 3, 4]) == [
        1,
        -1,
        2,
        -2,
        3,
        -3,
        4,
        -4,
    ]
    print("test 1 successful")


def test2():
    assert rearrange([3, 1, -2, -5, 2, -4]) == [3, -2, 1, -5, 2, -4]
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
