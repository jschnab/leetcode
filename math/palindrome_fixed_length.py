"""
leetcode 2217: Find palindrom with fixed length.

Given an integer array `A` and a positing integer `length`, return an array
`R` where `R[i]` is either the `A[i]`th smallest positive palindrome of length
`length` or -1 if no such palindrome exists.

A palindrome is a number with the same sequence of digits when read forward or
backward. Palindromes cannot have leading zeros.
"""
import math


def palindrome(n, length):
    """
    Return the nth palindrome of a specific length.

    We only determine half the digits that make up the palindrome because
    these digits are repeated.

    We also notice that palindromes can be built with a power of ten. Because
    we are interested in ordered palindromes, we can add n to the power of 10.

    :param int n: Index of the desired palindrome.
    :param int length: Number of digits in the palindrome.
    :returns (int): Palindrome.
    """
    # if length is odd, we want the power (length - 1) / 2
    # if length is even, we want the power (length - 1) / 2 - 1
    power = 10 ** math.floor((length - 1) / 2)

    # we use n - 1 to convert 1-indexing to 0-indexing
    half_pal = list(str(n - 1 + power))

    # we assemble the two halfs of the palindrome
    pal = half_pal + half_pal[-1 - length % 2::-1]
    return int("".join(pal))


def nth_palindrome(A, length):
    """
    We notice that given a number length L, there can only be
    9 * 10 ** floor((L - 1) / 2) palindromes. For example, there are 90
    palindromes made of 3 digits.

    :param list[int] A: Array of queries.
    :param int length: Number of digits in the palindrome.
    :returns (list[int]): nth palindrome, else -1.
    """
    result = []
    for i in A:
        if i <= 9 * 10 ** math.floor((length - 1) / 2):
            result.append(palindrome(i, length))
        else:
            result.append(-1)
    return result


def test1():
    assert nth_palindrome([1, 2, 3, 90], 3) == [101, 111, 121, 999]
    print("test 1 successful")


def test2():
    assert nth_palindrome([2, 4, 6, 10000], 4) == [1111, 1331, 1551, -1]
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
