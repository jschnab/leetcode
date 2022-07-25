"""
leetcode 2275: Largest combination with bitwise AND greater than zero.

The bitwise AND of an array A is the bitwise AND of all integers in A.

Given an array of positive integers A, evaluate the bitwise AND of every
combination of numbers of A. Each number in A can only be used once in each
combination.

Return the size of the largest combination of A with a bitwise AND greater than
0.
"""


def largest_combination(A):
    """
    Largest combination of array elements with bitwise AND greater than zero.

    We iterate over all bit positions and calculate how many elements of A have
    this bit position set, and keep track of the maximum number of elements.

    :param list(int) A: Array of candidates for combination.
    :returns (int): Result.
    """
    result = 0
    for i in range(24):  # range of number of bits used to encode integers in A
        s = 0
        for c in A:
            s += c & (1 << i) > 0
        result = max(result, s)
    return result


def test1():
    assert largest_combination([16, 17, 71, 62, 12, 24, 14]) == 4
    print("test 1 successful")


def test2():
    assert largest_combination([8, 8]) == 2
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
