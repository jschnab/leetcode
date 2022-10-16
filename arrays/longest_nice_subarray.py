"""
leetcode 2401: longest nice subarray

We are given an array A containing positive integers.

We call a subarray of A 'nice' if the bitwise AND of every pair of elements
that are in different positions in the subarray is equal to 0. This means that
a subarray of length 1 is nice.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.
"""


def nice(A):
    """
    We use a sliding window and calculate the bitwise OR of all elements in a
    window and check it's 0 (equivalent to bitwise AND of every pair of
    element).

    We grow the window on the right as long as OR of all elements is 0. If it
    is not 0, we shrink the window from the left until it is 0, or the window
    is empty.
    """
    maxi = 1
    current = 1  # current maximum
    s = A[0]
    i = 0  # position of left boundary of window

    for j in range(1, len(A)):  # position of right boundary of window
        if not s & A[j]:  # if A[j] AND all elements is 0, add A[j]
            s |= A[j]
            current += 1
            maxi = max(maxi, current)
        else:  # remove elements from the left of the window
            while i < j and s & A[j]:  # until window empty or AND elements = 0
                s ^= A[i]
                current -= 1
                i += 1
            s |= A[j]
            current += 1

    return maxi


def test1():
    assert nice([1, 3, 8, 48, 10]) == 3
    print("test 1 successful")


def test2():
    assert nice([3, 1, 5, 11, 13]) == 1
    print("test 2 successful")


def test3():
    assert nice([1, 2, 4, 9, 16]) == 4
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
