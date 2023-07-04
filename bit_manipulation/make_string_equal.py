"""
leetcode 2546: apply bitwise operations to make strings equal

We are given two binary strings S and T of the same length n. We can do the
following operations on S any number of times:

    1. Choose two different indices i and j where 0 <= i, j < n.
    2. Simultaneously, replace S[i] with S[i] OR S[j] and S[j] with S[i] XOR S[j].

For example, if S = "0110", we can choose i = 0 and j = 2, then we obtain "1110".

Return true if we can make S equal to T, or false otherwise.
"""


def equal(S, T):
    """
    Let's draw a truth table:

    i  j  i|j  i^j
    0  0   0    0
    0  1   1    1
    1  0   1    1
    1  1   1    0

    We are not interested in cases where i and j are both 0, because in these
    cases there is not transformation.

    To transform 0 into 1, we need i and j to be different (does not matter
    which one is 1 and which one is 0).

    To transform a 1 into 0, we need i and j to be both 1, and then j becomes 0.

    We then realize that if S is all 0 and T has at least one 1, the
    transformation is impossible. Conversely, if T is all 0 and S has at least
    one 1, the transformation is also impossible, In all other cases, we can
    transform S into T.
    """
    # with Python 3.10, use the .bit_count() method.
    s1 = S.count("1")
    t1 = T.count("1")
    if (s1 == 0 and t1 > 0) or (s1 > 0 and t1 == 0):
        return False
    return True


def test1():
    assert equal("1010", "0110")
    print("test 1 successful")


def test2():
    assert equal("11", "00") is False
    print("test 2 successful")


if __name__ == "__main__":
    test1()
    test2()
