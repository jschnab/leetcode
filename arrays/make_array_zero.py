"""
leetcode 2357: make array zero by subtracting equal amounts

We are given a non-negative integer array A. In one operation, we must:

* choose a positive integer x such that x is less than or equal to the smallest
  non-zero element in A
* subtract x from every positive element in A

Return the minimum number of operations to make every element in A equal to
zero.
"""


def make_array_zero(A):
    """
    Every step, we take the smallest element in A and subtract it from the
    other elements. To get all elements to zero, we will have to repear the
    operation as many times as there are unique non-zero elements in A.
    """
    return len(set(A) - {0})


def test1():
    assert make_array_zero([1, 5, 0, 3, 5]) == 3
    print("test 1 successful")


def test2():
    assert make_array_zero([0]) == 0
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
