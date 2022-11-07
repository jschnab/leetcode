"""
leetcode 2414: length of the longest alphabetical continuous substring

An alphabetical continuous string is a string consisting of consecutive letters
in the alphabet. In other words, it is any substring of the string 'abcd...'.

Given a string s consisting of lowercase letters only, return the length of the
longest alphabetical continuous substring.
"""


def longest_string(s):
    """
    Using two string indices, we iterate through the string: the first index is
    the start of a new substring, the second index is the end of the substring
    we try to extend as far as possible.

    Once we reach the end of a non-continuous substring, we record its length
    and move the first pointer at the place of the second.

    Time complexity: O(n).
    Space complexity: O(1).
    """
    result = 1  # at a minimum, a single letter
    i = 0
    while i < len(s) - 1:
        j = i + 1
        while j < len(s) and ord(s[j]) - ord(s[j - 1]) == 1:
            j += 1
        result = max(result, j - i)
        i = j
    return result


def test1():
    assert longest_string("abacaba") == 2
    print("test 1 successful")


def test2():
    assert longest_string("abcde") == 5
    print("test 2 successful")


def test3():
    assert longest_string("zzzzz") == 1
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
