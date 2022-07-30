"""
leetcode 2310: sum of numbers with units digit k

We are given two integers n and k.

We consider a set of positive integers with the following properties:
1. the units digit of each integer is k
2. the sum of the integers is n

Return the minimum possible size of such a set, or -1 if no such set exists.

The set can contain multiple instances of the same integer, and the sum of an
empty set is considered 0.

The units digit of a number is the rightmost digit of the number.
"""


def solution(n, k):
    """
    Because of property 1: n - m * k has 0 as a unit digit
    Because of property 2: m * k <= n

    We notice that the solution must be between 0 and 10. 0 is the solution if
    n is zero.

    We iterate over all numbers from 1 to 10 and check both problem properties.

    Time complexity: O(1). We only ever iterate from 1 to 10.
    Space complexity: O(1).
    """
    if n == 0:
        return 0
    for i in range(1, 11):
        if i * k % 10 == n % 10 and i * k <= n:
            return i
    return -1


def test1():
    assert solution(58, 9) == 2
    print("test 1 successful")


def test2():
    assert solution(37, 2) == -1
    print("test 2 successful")


def test3():
    assert solution(0, 7) == 0
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
