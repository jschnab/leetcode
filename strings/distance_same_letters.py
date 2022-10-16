"""
leetcode 2399: check distances between same letters

We are given a string S consisting of only lowercase english letters, where
each letter in S appears exactly twice. We are also ggiven an integer array D
(distance) of length 26.

Each letter in the alphabet is numbered from 0 to 25 (a=0, b=1, etc.).

In a well-spaced string, the number of letters between the two occurrences of
the ith letter is D[i]. If the ith letter does not appear in S, then D[i] can
be ignored.

Return true if S is a well-spaced string, otherwise return false.
"""


def well_spaced(S, D):
    """
    We record the position in S of the first occurence of a letter. If we
    encounter the letter a second time, we check their spacing.

    Time complexity: O(1), the string has at most 52 characters and we iterate
        through it once, in addition to generate a list of constant size.
    Space complexity: O(1), we store the position of each letter in a list as
        long as the alphabet.
    """
    seen = [None] * 26
    for i, c in enumerate(S):
        if seen[ord(c) - ord("a")] is None:
            seen[ord(c) - ord("a")] = i
        else:
            if i - seen[ord(c) - ord("a")] != D[ord(c) - ord("a")] + 1:
                return False
    return True


def test1():
    S = "abaccb"
    D = [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0]
    assert well_spaced(S, D) is True
    print("test 1 successful")


def test2():
    S = "aa"
    D = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0]
    assert well_spaced(S, D) is False
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
