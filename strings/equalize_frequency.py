"""
leetcode 2423: remove letter to equalize frequency

We are given a string S, consisting of lowercase English letters. We need to
select one index and remove the letter at that index from S so that the
frequency of every letter present in S is equal.

Return True if it is possible to remove one letter so that the frequency of all
letters in S are equal, and False otherwise.
"""
from collections import Counter


def eq_freq(S):
    count = Counter(S)
    for char in S:
        count[char] -= 1
        if len(set(count.values()) - {0}) == 1:
            return True
        count[char] += 1
    return False


def test1():
    assert eq_freq("abcc") is True
    print("test 1 successful")


def test2():
    assert eq_freq("aazz") is False
    print("test 2 successful")


def test3():
    assert eq_freq("xy") is True
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
