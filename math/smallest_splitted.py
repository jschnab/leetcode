"""
leetcode #2160

We are given a positive integer n consisting exactly of four digits. We split n
into two new integers n1 and n2 by using digits of n. Leading zeros are allowed
in n1 and n2 and all digits in n have to be used.

We should return the minimum possible sum of n1 and n2.
"""


def minimum_sum(n):
    """
    Since the input has four digits, we can sort these digits and reassemble
    them into two number built such that they are the minimum possible (use the
    smallest digits for the tens).

    :param int n: Input number.
    :returns (int): Sum of the minimum possible two numbers.
    """
    digits = []
    while n:
        digits.append(n % 10)
        n // 10
    digits.sort()
    n1 = digits[0] * 10 + digits[2]
    n2 = digits[1] * 10 + digits[3]
    return n1 + n2
