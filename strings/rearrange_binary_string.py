"""
leetcode 2380: time needed to rearrange binary string

We are given a binary string S. In one second, all occurrences of "01" are
simultaneously replaced with "10". This process repeats until no occurrences of
"01" exist.

Return the number of seconds needed to complete this process.
"""


def rearrange(S):
    """
    As we iterate through S, we count how many zeros we've seen and how much
    time we've spent rearranging the string so far. If the current character is
    1, we need at least seconds + 1 seconds, but not less than #zeros seconds.

    S       10011111000100001
    zeros   01222222345567899
    seconds 00023456666777779

    Time complexity: O(n)
    Space complexity: O(1)
    """
    seconds = 0
    zeros = 0
    for c in S:
        zeros += c == "0"
        if c == "1" and zeros:
            seconds = max(zeros, seconds + 1)
    return seconds


def test1():
    assert rearrange("0110101") == 4
    print("test 1 successful")


def test2():
    assert rearrange("11100") == 0
    print("test 2 successful")


def test3():
    assert rearrange("10011111000100001") == 9
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
