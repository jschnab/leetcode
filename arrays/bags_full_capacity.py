"""
leetcode 2279: Maximum bags with full capacity of rocks.

You have n bags and two integer arrays 'capacity' and 'rocks'. The ith bag can
hold a maximum capacity of capacity[i] rocks and currently contains rocks[i]
rocks. You are also given an integer 'additional', the number of additional
rocks you can place in any of the bags.

Return the maximum number of bags that could have full capacity after placing
the additional rocks in some bags.
"""


def max_bags(capacity, rocks, additional):
    """
    Number of bags that could have full capacity.

    :param list(int) capacity: Bags capacity.
    :param list(int) rocks: Number of rocks in bags.
    :param int additional: Number of available additional rocks.
    :returns (int): Number of full bags.
    """
    # how many rocks we could add to each bag, sorted from most least to most
    # full
    diff = sorted([c - r for c, r in zip(capacity, rocks)], reverse=True)

    # while there are still bags to fill, we fill them, starting with the
    # fullest bags
    while diff and diff[-1] <= additional:
        additional -= diff.pop()

    # subtract number of still-not-full bags from total number of bags
    return len(rocks) - len(diff)


def test1():
    assert max_bags([2, 3, 4, 5], [1, 2, 4, 4], 2) == 3
    print("test 1 successful")


def test2():
    assert max_bags([10, 2, 2], [2, 2, 0], 100) == 3
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
