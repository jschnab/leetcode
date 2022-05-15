"""
Given an integer array A, return the number with the value closest to 0 in A.
If there are multiple answers, return the number with the largest value.
"""


def closest_zero(A):
    """
    There may be up to 2 equivalents answers: a number and its opposite, in
    which case the positive number wins.

    :param list A: Array of integers.
    :returns (int): Number closest to zero.
    """
    diff = float("inf")
    candidates = []
    for i in A:
        absolute = abs(i)
        if absolute < diff:
            candidates = [i]
            diff = absolute
        elif absolute == diff:
            candidates.append(i)
    return max(candidates)


def test1():
    assert closest_zero([-4, -2, 1, 4, 8]) == 1
    print("test 1 successful")


def test2():
    assert closest_zero([2, -1]) == -1
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
