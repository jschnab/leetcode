"""
leetcode 2516: take k of each character from left and right

We are given a string S consisting of characters 'a', 'b', and 'c', and a
non-negative integer k. Each minute, we may take either the leftmost character
of S, or the rightmost character of S.

Return the minimum number of minutes needed to take at least k of each
character, or return -1 if it is not possible to take k of each character.
"""


def take_char(S, k):
    counts = [0, 0, 0]
    for char in S:
        counts[ord(char) - ord("a")] += 1
    if not all(c >= k for c in counts):
        return -1
    window_length = -1
    i = j = 0
    while i < len(S):
        counts[ord(S[i]) - ord("a")] -= 1
        while counts[ord(S[i]) - ord("a")] < k:
            counts[ord(S[j]) - ord("a")] += 1
            j += 1
        window_length = max(window_length, i - j + 1)
        i += 1
    return len(S) - window_length


def test1():
    assert take_char("aabaaaacaabc", 2) == 8
    print("test 1 successful")


def test2():
    assert take_char("a", 1) == -1
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
