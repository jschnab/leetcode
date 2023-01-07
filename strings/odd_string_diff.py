"""
leetcode 2451: odd string difference

We are given an array of equal-length strings 'words'. Assume the length of
each string is n.

Each string words[i] can be converted into a difference integer array
difference[i] of length n - 1 where difference[i][j] = words[i][j+1] -
words[i][j] and 0 <= j <= n- 2. Note that the difference between two letters is
the difference between their positions in the alphabet i.e. the position of 'a'
is 0, 'b' is 1, and 'z' is 25.

For example, the sting "acb" has the difference integer array [2, -1].

All the strings in words have the same difference integer array except one. You
should find that string.

Return the string in words that has a different difference integer array.
"""


def odd_string(words):
    diff = [[ord(w[i+1]) - ord(w[i]) for i in range(len(w)-1)] for w in words]
    if diff[0] == diff[1]:
        d = diff[0]
    else:
        d = diff[2]
    for i, w in enumerate(diff):
        if w != d:
            return words[i]


def test1():
    words = ["adc", "wzy", "abc"]
    assert odd_string(words) == "abc"
    print("test 1 successful")


def test2():
    words = ["aaa", "bob", "ccc", "ddd"]
    assert odd_string(words) == "bob"
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
