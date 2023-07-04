"""
leetcode 80: remove duplicates from sorted array II

Given an integer array A sorted in non-decreasing order, remove some duplicates
in place such that each unique element appears at most twice. The relative
order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, we
must instead have the result placed in the first part of the array A. More
formally, if there are k elements after removing the duplicates, then the first
k elements of A should hold the final result. It does not matter what we leave
beyond the first k elements.

The solution should use constant memory with respect to input size.

Return k after placing the final result in the first k slots of A.
"""

def remove_dups(A):
    i = 0
    for n in A:
        if i < 2 or A[i - 2] < n:
            A[i] = n
            i += 1
    return i


def test1():
    A = [1, 1, 1, 2, 2, 3]
    k = 5
    assert remove_dups(A) == k
    assert A[:k] == [1, 1, 2, 2, 3]
    print("test 1 successful")


def test2():
    A = [0, 0, 1, 1, 1, 1, 2, 3, 3, 3]
    k = 7
    assert remove_dups(A) == k
    assert A[:k] == [0, 0, 1, 1, 2, 3, 3]
    print("test 2 successful")


if __name__ == "__main__":
    test1()
    test2()
