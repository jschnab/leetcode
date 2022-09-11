"""
leetcode 2364: count number of bad pairs

We are given an integer array A. A pair of indices (i, j) is a bad pair if i <
j and j - i != A[j] - A[i].

Return the total number of bad pairs in A.
"""


def pairs(A):
    """
    Bad pair: A[i] - i != A[j] - j
    Good pair: A[i] - i == A[j] - j

    For every index i of A, A[i] is in a good pair with any previous number
    equal to A[i] - i. The rest are bad pairs.
    """
    result = 0
    d = {}
    for i in range(len(A)):
        result += i - d.get(A[i] - i, 0)
        d[A[i] - i] = d.get(A[i] - i, 0) + 1
    return result


def test1():
    assert pairs([4, 1, 3, 3]) == 5
    print("test 1 successful")


def test2():
    assert pairs([1, 2, 3, 4, 5]) == 0
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
