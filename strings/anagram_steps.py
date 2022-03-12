"""
leetcode 2186: Minimum number of steps to make two strings anagrams.

Given two strings a and b, in one step we can append any character to a or b.

We determine the minimum number of steps to make a and b anagrams of each
other.

An anagram of a string is a string that contains the same characters with a
different (or identical) ordering.
"""

from collections import Counter


def steps(a, b):
    """
    We count letters in a and b, then calculate the difference in letter counts
    between a and b.

    Time complexity: We iterate over all characters of a and b, then iterate
    over their unique characters, so the overall complexity is
    O(len(a)+len(b)).
    """
    count_a = Counter(a)
    count_b = Counter(b)
    result = 0
    counted = set()
    for letter, count in count_a.items():
        result += abs(count_b.get(letter, 0) - count)
        counted.add(letter)
    for letter, count in count_b.items():
        if letter not in counted:
            result += abs(count_a.get(letter, 0) - count)
    return result


def test1():
    assert steps("leetcode", "coats") == 7
    print("test 1 successful")


def test2():
    assert steps("night", "thing") == 0
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
