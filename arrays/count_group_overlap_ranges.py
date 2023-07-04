"""
leetcode 2580: count ways to group overlapping ranges

We are given a 2D integer array A where A[i] = [start, end] denotes that all
integers between start and end (both inclusive) are contained in the ith range.

We have to split A into two (possibly empty) groups such that:

* Each range belongs to exactly one group.
* Any two overlapping ranges must belong to the same group.

Two ranges are said to be overlapping if there exists at least one integer that
is present in both ranges.

Return the total number of ways to split A into two groups. Since the answer
may be very large, return it modulo 10^9 + 7.
"""

def count(A):
    """
    We sort ranges so we can easily identify overlaps (any overlap must involve
    adjacent ranges).

    The maximum number of groups is obtained when there is no overlap, so there
    are as many groups as distinct ranges. We count distinct ranges then
    decrement the number for every range overlap.
    """
    A.sort(key=lambda x: x[0])
    # Index of the range with the highest right boundary of the group.
    # This ensures we identify overlaps when some ranges enclose others in the
    # same group.
    i = 0
    ngroups = len(A)
    for j in range(1, len(A)):
        # If there is an overlap, decrease the number of groups.
        if A[j][0] <= A[i][1]:
            ngroups -= 1
            # Ensure i points to the range with the highest right boundary.
            if A[i][1] < A[j][1]:
                i = j
        else:
            i = j
    return pow(2, ngroups, 1000000007)


def test1():
    A = [[6, 10], [5, 15]]
    assert count(A) == 2
    print("test 1 successful")


def test2():
    A = [[1, 3], [10, 20], [2, 5], [4, 8]]
    assert count(A) == 4
    print("test 2 successful")


def test3():
    A = [
        [34, 56], [28, 29], [12, 16], [11, 48], [28, 54], [22, 55], [28, 41],
        [41,44]
    ]
    assert count(A) == 2
    print("test 3 successful")


def test4():
    A = [[5, 11], [20, 22], [1, 3], [21, 22], [11, 11]]
    assert count(A) == 8
    print("test 4 successful")


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
