"""
leetcode 2543: check if point is reachable

There exists an infinitely large grid. We are currently at point (1, 1) and we
need to reach point (X, Y) using a finite number of steps.

In one step, we can move from point (x, y) to any one of the following points:

* (x, y - x)
* (x - y, x)
* (2 * x, y)
* (x, 2 * y)

Given two integers X and Y, representing the x and y coordinates of our final
position, return true if we can reach the point from (1, 1), using some number
of steps, or false otherwise.
"""
import math
import sys


def reachable(x, y):
    """
    We reverse the problem and see if we can reach (1, 1) from (x, y).
    """
    if x == y == 1:
        return True
    if x < y:
        return reachable(x, y - x)
    if x > y:
        return reachable(x - y, y)
    if x % 2 == 0:
        return reachable(x // 2, y)
    if y % 2 == 0:
        return reachable(x, y // 2)
    return False


def reachable_gcd(x, y):
    """
    We recognize the calculation of the GCD of x and y in the moves (x, y - x)
    and (x - y, y). Thus, these moves do not change the GCD. For the moves
    (2 * x, y) and (x, 2 * y), the GCD either stays the same or is doubled.

    GCD(1, 1) = 1. Between (1, 1) and (x, y), the GCD can either remain the
    same or be doubled at least once. Therefore, we can reach (x, y) from (1,
    1) only if GCD(x, y) is a power of 2.
    """
    if sys.version_info.major >= 3 and sys.version_info.minor >= 10:
        return math.gcd(x, y).bit_count() == 1
    return bin(math.gcd(x, y)).count("1") == 1


def test1():
    assert not reachable(6, 9)
    assert not reachable_gcd(6, 9)
    print("test 1 successful")


def test2():
    assert reachable(4, 7)
    assert reachable_gcd(4, 7)
    print("test 2 successful")


if __name__ == "__main__":
    test1()
    test2()
