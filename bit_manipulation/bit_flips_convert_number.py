"""
leetcode 2220: Minimum bit flips to convert number.

A bit flip of a number x is choosing a bit in the binary representation of x
and flipping it from 0 to 1 or 1 to 0.

Given two integers A and B, return the minimum number of bit flips to convert
A to B.
"""


def bit_flips(A, B):
    return bin(A ^ B).count("1")


def test1():
    assert bit_flips(10, 7) == 3
    print("test 1 successful")


def test2():
    assert bit_flips(3, 4) == 3
    print("test 2 successful")


def test3():
    assert bit_flips(5, 5) == 0
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
