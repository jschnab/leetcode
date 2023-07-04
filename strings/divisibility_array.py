"""
leetcode 2575: find the divisibility array of a string

We are given a string S of length n consisting of digits, and a positive
integer m. The divisibility array D of S is an integer array of length n such
that:

* D[i] = 1 if the numeric value of S[0,...i] is divisible by m
* D[i] = 0 otherwise

Return the divisibility array of S.
"""


def div_arr(S, m):
    result = []
    mod = 0
    for char in S:
        mod = (mod * 10 + ord(char) - ord("0")) % m
        if mod == 0:
            result.append(1)
        else:
            result.append(0)
    return result


def test1():
    assert div_arr("998244353", 3) == [1, 1, 0, 0, 0, 1, 1, 0, 0]
    print("test 1 successful")


def test2():
    assert div_arr("1010", 10) == [0, 1, 0, 1]
    print("test 2 successful")


if __name__ == "__main__":
    test1()
    test2()
