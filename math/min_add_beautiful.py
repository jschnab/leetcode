"""
leetcode 2457: minimum addition to make integer beautiful

We are given two positive integers n and target.

An integer is considered beautiful if the sum of its digits is less than or
equal to target.

Return the minimum non-negative integer x such that n + x is beautiful. The
input can be assumed to always have a solution.
"""


def beautiful(n, target):
    def sum_digits(n):
        result = 0
        while n > 0:
            result += n % 10
            n //= 10
        return result

    x = n
    p = 1
    while sum_digits(x) > target:
        x = (x // 10**p + 1) * 10**p
        p += 1
    return x - n


def test1():
    assert beautiful(16, 6) == 4
    print("test 1 successful")


def test2():
    assert beautiful(467, 6) == 33
    print("test 2 successful")


def test3():
    assert beautiful(1, 1) == 0
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
