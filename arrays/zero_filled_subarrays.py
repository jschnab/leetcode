"""
leetcode 2348: number of zero-filled subarrays

Given an integer array A, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within the array.
"""


def zero_subarrays(A):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    result = 0
    i = 0
    while i < len(A):
        n_zeros = 0
        while i < len(A) and A[i] == 0:
            n_zeros += 1
            i += 1
        result += n_zeros * (n_zeros + 1) // 2
        i += 1
    return result


def test1():
    assert zero_subarrays([1, 3, 0, 0, 2, 0, 0, 4]) == 6
    print("test 1 successful")


def test2():
    assert zero_subarrays([0, 0, 0, 2, 2, 0, 0])
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
