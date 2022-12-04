"""
leetcode 2443: sum of number and its reverse

Given a non-negative integer n, return 'true' if n can be expressed as the sum
of any non-negative integer and its reverse, or false otherwise.
"""


def rev(n):
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n //= 10
    return result


def sum_reverse(n):
    for i in range(n // 2, n + 1):
        if i + rev(i) == n:
            return True
    return False


def test1():
    assert sum_reverse(443) is True
    print("test 1 successful")


def test2():
    assert sum_reverse(63) is False
    print("test 2 successful")


def test3():
    assert sum_reverse(181) is True
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
