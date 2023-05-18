"""
leetcode 2514: count anagrams

We are given a string s containing one or more words.
Every consecutive pair of words is separated by a single space.

A string t is an anagram of string s if the ith word of t is a permutation of
the ith word of s.

For example, "abc dfe" is an anagram of "abc def" but "def cab" and "adc bef"
are not.

Return the number of distinct anagrams of s. Since the answer may be very
large, return it modulo 1e9 + 7.
"""
import math
from collections import Counter


def anagrams(s):
    """
    The number of permutation on a string of length L is L! (factorial L).

    Strings can have one or more repetitions of one or more characters, so we
    count the number of characters and divide L! by c! where c is the count of
    each character of a string.
    """
    result = 1
    for w in s.split():
        counts = Counter(w)
        cnt = math.factorial(len(w))
        for c in counts.values():
            cnt //= math.factorial(c)
        result = result * cnt % 1000000007
    return result


def test1():
    assert anagrams("too hot") == 18
    print("test 1 successful")


def test2():
    assert anagrams("aa") == 1
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
