"""
leetcode 2311: longest binary subsequence less than or equal to k

We are given a binary string S and a positive integer k.

Return the length of the longest subsequence of S that makes up a binary number
less than or equal to k.

The subsequence can contain leading zeroes.

The empty string is considered to be equal to 0.

A subsequence is a string that can be derived from another string by deleting
some or no characters without changing the order of the remaining characters.
"""


def longest_subseq(s, k):
    """
    The solution must at least contain all 0s, because they do not contribute to
    making a number greater than k.

    Then, we add 1s, one by one from least significant to most significant
    (right to left in the string), until we reach a number greater than k.

    Time complexity: O(n) where n is the length of the bit string.
    Space complexity: O(1).
    """
    length = s.count("0")
    sum_ = 0
    for i, c in enumerate(s[::-1]):
        if c == "1":
            sum_ += 1 << i
            if sum_ <= k:
                length += 1
            else:
                break
    return length


def test1():
    assert longest_subseq("1001010", 5) == 5
    print("test 1 successful")


def test2():
    assert longest_subseq("00101001", 1) == 6
    print("test 2 successful")


def test3():
    assert longest_subseq("001010101011010100010101101010010", 93951055) == 31
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
