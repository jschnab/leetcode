"""
leetcode 2210: Count hills and valleys in an array.

Given an array A of integers, an index i is part of a hill if the closest
non-equal neighbors of A[i] are smaller than A[i]. Similarly, an index i is
part of a valley if the closest non-equal neighbors of A[i] are greater than
A[i]. Adjacent indices i and j are part of the same valley or hill if
A[i] == A[j].

Return the number of hills and valleys in A.
"""


def hills_valleys(A):
    """
    We use two pointers and iterate once through the array.

    Time complexity: O(n).
    Space complexity: O(1).
    """
    result = 0
    i = 0
    for j in range(1, len(A) - 1):
        if A[i] < A[j] and A[j] > A[j + 1] or A[i] > A[j] and A[j] < A[j + 1]:
            result += 1
            i = j
    return result


def test1():
    assert hills_valleys([2, 4, 1, 1, 6, 5]) == 3
    print("test 1 successful")


def test2():
    assert hills_valleys([6, 6, 5, 5, 4, 1]) == 0
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
