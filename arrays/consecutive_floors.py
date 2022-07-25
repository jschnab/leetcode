"""
leetcode 2274: Maximum consecutive floors without special floors.

Alice manages a company and has rented some floors of a building as office
space. Alice has decided some of these floors should be special, used for
relaxation only.

Given two integers 'bottom' and 'top' that indicate that Alice rented all
floors from bottom to top (inclusive), and the integer array 'special', where
special[i] is a special floor that Alice has designated for relaxation, return
the maximum number of consecutive floors without a special floor.
"""


def max_consecutive(bottom, top, special):
    """
    Maximum number of consecutive floors without a special floor.

    :param int bottom: Lowest rented floor.
    :param int top: Highest rented floor.
    :param list(int) special: Floors for relaxation.
    :returns (int): Result.
    """
    special.sort()
    result = special[0] - bottom
    for i in range(1, len(special)):
        result = max(result, special[i] - special[i - 1] - 1)
    result = max(result, top - special[-1])
    return result


def test1():
    assert max_consecutive(2, 9, [4, 6]) == 3
    print("test 1 successful")


def test2():
    assert max_consecutive(6, 8, [7, 6, 8]) == 0
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
