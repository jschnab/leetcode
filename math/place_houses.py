"""
leetcode 2320: count number of ways to place houses

There is a street with n * 2 plot where there are n plots on each side of the
street. The plots on each side are numbered from 1 to n. On each plot, a house
can be placed.

Return the number of ways houses can be places such that no two houses are
adjacent to each other on the same side of the street. Since the answer may be
very large, return it modulo 1e9 + 7.

Note that if a house is placed on the ith plot on one side of the street, a
house can also be placed on the ith plot on the other side of the street.
"""


def houses(n):
    """
    """
    # the number of houses on one side forms a fibonacci series
    a = 1
    b = 1
    for i in range(1, n + 1):
        c = a + b
        a = b
        b = c
    return c ** 2 % 1000000007


def test1():
    assert houses(1) == 4
    print("test 1 successful")


def test2():
    assert houses(2) == 9
    print("test 2 successful")


def test3():
    assert houses(6) == 441
    print("test 2 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
