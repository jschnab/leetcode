"""
leetcode 2425: bitwise xor of all pairs

We are given two arrays A and B, consisting of non-negative integers. There
exists another array, C, which contains the bitwise XOR or all pairs of
integers between A and B (every integer in A is paired with every integer in B
exactly once).

Return the bitwise XOR of all integers in C.
"""


def xor_pairs(A, B):
    """
    An even number of XOR of operations on a number will make it equal to 0, so
    if we generate an even number of pairings, the paired number is nullified.

    Therefore, we calculate XOR on A only if the length of B is odd, and we
    calculate XOR on B only if the length of A is odd.
    """
    n1 = len(A)
    n2 = len(B)
    result = 0
    if n1 & 1:
        for x in B:
            result ^= x
        if n2 & 1:
            for x in A:
                result ^= x
    elif n2 & 1:
        for x in A:
            result ^= x
    return result


def test1():
    assert xor_pairs([2, 1, 3], [10, 2, 5, 0]) == 13
    print("test 1 successful")


def test2():
    assert xor_pairs([1, 2], [3, 4]) == 0
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
