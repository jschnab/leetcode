"""
leetcode 2405: optimal partition of string

Given a string S, partition the string into one or more substrings such that
the characters in each substring are unique. That is, no letter appears in a
single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.
"""


def partition(S):
    """
    We keep track of the boundaries of a partition, while trying to extend a
    partition from the right. Once we find a character already present in the
    partition, we start a new partition.
    """
    count = 1
    i = 0
    j = 1
    unique = {S[0]}
    while j < len(S):
        if S[j] not in unique:
            unique.add(S[j])
        else:
            count += 1
            i = j
            unique = {S[i]}
        j += 1
    return count


def test1():
    assert partition("abacaba") == 4
    print("test 1 successful")


def test2():
    assert partition("sssss") == 5
    print("test 2 successful")


def test3():
    assert partition("x") == 1
    print("test 3 successful")


def test4():
    assert partition("abcdaef") == 2
    print("test 4 successful")


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
