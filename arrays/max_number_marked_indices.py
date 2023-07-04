"""
leetcode 2576: find the maximum number of marked indices

We are given an integer array A. Initially, all the indices are unmarked. We
are allowed to make this operation any number of times:

* Pick two different unmarked indices i and j such that 2 * nums[i] <= nums[j],
  then mark i and j.

Return the maximum possible number of marked indices in nums using the above
operation any number of times.
"""

def marked_indices(A):
    A.sort()
    i = 0
    for j in range(len(A) - len(A) // 2, len(A)):
        if 2 * A[i] <= A[j]:
            i += 1
    return 2 * i


def test1():
    assert marked_indices([3, 5, 2, 4]) == 2
    print("test 1 successful")


def test2():
    assert marked_indices([9, 2, 5, 4]) == 4
    print("test 2 successful")


if __name__ == "__main__":
    test1()
    test2()
