"""
leetcode 2578: split with minimum sum

Given a positive integer N, split it into two non-negative integers A and B
such that:

* The concatenetation of A and B is a permutation of N.
* A and B can contain leading zeros.

Return the minimum possible sum of A and B.
"""


def split(N):
    S = "".join(sorted(str(N)))
    return int(S[::2]) + int(S[1::2])


def test1():
    assert split(4325) == 59
    print("test 1 successful")


def test2():
    assert split(687) == 75
    print("test 2 successful")


if __name__ == "__main__":
    test1()
    test2()
