"""
leetcode 2375: construct smallest number from DI string

We are given a string S of length n consisting of the characters 'D' meaning
decreasing and 'I' meaning increasing.

A string N of length n + 1 is created using the following conditions:

* N consists of the digits '1' to '9' where each digit is used at most once
* if S[i] == 'I', then N[i] < N[i + 1]
* if S[i] == 'D', then N[i] > N[i + 1]

Return the lexicographically smallest possible string N that meets the
conditions.
"""


def smallest_string(S):
    """
    We start with a list of increasing digits (as characters), starting from 1
    because we are trying to build the lexicographically smallest string.

    We iterate through a list of S characters and every time we encounter an I,
    we flip characters between the last I and the current I (excluding the
    current position because it's increasing).
    """
    result = list("123456789")
    i = 0
    # add I to make sure we encouter I at least once (e.g. S = "DDDD")
    for j, c in enumerate(S + "I", 1):
        if c == "I":
            # avoid trivial flips
            if j - i > 1:
                result[i:j] = result[i:j][::-1]
            i = j
    # cut out excedentary characters
    return "".join(result)[:i]


def test1():
    assert smallest_string("IIIDIDDD") == "123549876"
    print("test 1 successful")


def test2():
    assert smallest_string("DDD") == "4321"
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
