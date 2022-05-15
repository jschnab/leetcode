"""
leetcode 2255: Count prefixes of a given string.

Given an array of strings P and a string S, where P[i] and S are made only of
ASCII lowercase letters, return the number of strings in P that are a prefix of
S.

A prefix of a string is a substring that occurs at the beginning of the string.
A substring is a contiguous sequence of characters withing a string.
"""


def count_prefixes(P, S):
    return sum(1 for w in P if S.startswith(w))


def test1():
    P = ["a", "b", "c", "ab", "bc", "abc"]
    S = "abc"
    assert count_prefixes(P, S) == 3
    print("test 1 successful")


def test2():
    P = ["a", "a"]
    S = "aa"
    assert count_prefixes(P, S) == 2
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
