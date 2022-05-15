"""
leetcode 2256: Minimum average difference.

We are given an integer array A.

The average difference of index i is the absolute difference between the
average of the first i + 1 elements of A and the last n - i - 1 elements.
Both averages are rounded down to the nearest integer.

Return the index with the minimum average difference. If there are multiple
solutions, return the smallest one.

The average of n elements is the sum of the n elements divided (integer div) by
n. The average of 0 elements is 0.
"""


def min_average_diff(A):
    # calculate for index 0 before iteration
    n1 = 1
    n2 = len(A) - 1
    s1 = avg1 = A[0]
    s2 = sum(A[1:])
    # there could be a single element in A, then n2 = avg2 = 0
    if n2 > 0:
        avg2 = s2 // n2
    else:
        avg2 = 0
    min_diff = abs(avg1 - avg2)

    # iterate over indices 1 through len(A) - 1
    # we move elements of A from s2 to s1 then calculat min avg diff
    result = 0
    for i in range(1, len(A)):
        s1 += A[i]
        n1 += 1
        avg1 = s1 // n1
        s2 -= A[i]
        n2 -= 1
        # check that n2 is not zero, occurring on the last iteration
        if n2 > 0:
            avg2 = s2 // n2
        else:
            avg2 = 0
        if abs(avg1 - avg2) < min_diff:
            result = i
            min_diff = abs(avg1 - avg2)
    return result


def test1():
    assert min_average_diff([2, 5, 3, 9, 5, 3]) == 3
    print("test 1 successful")


def test2():
    assert min_average_diff([0]) == 0
    print("test 2 successful")


def test3():
    assert min_average_diff([3, 2, 1]) == 1
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
