from math import sqrt, trunc


def closest_divisors(x):
    """
    Given an integer x, find the closest two integers (in absolute difference)
    whose product equals x + 1 or x + 2. Return them in any order.

    Leetcode problem 1362

    Time complexity: O(sqrt(x))
    Space complexity: O(1)

    :param int x:
    :return tuple:
    """
    for i in range(trunc(sqrt(x+2)), 0, -1):
        if (x + 1) % i == 0:
            return i, (x + 1) // i
        if (x + 2) % i == 0:
            return i, (x + 2) // i


if __name__ == "__main__":
    print(closest_divisors(123))
    print(closest_divisors(8))
