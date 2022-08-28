"""
leetcode 348: maximum sum of a pair with equal sum of digits

We are given an array A consisting of positive integers. We can choose two
indices i and j such that i != j and the sum of digits of A[i] and A[j] are
equal.

Return the maximum value of A[i] + A[j] that we can obtain over all possible i
and j that satisfy the conditions.
"""


def max_pair(A):
    """
    This is a variation of the 'two sum' problem.

    Time complexity: O(n).
    Space complexity: O(m) where m is the maximum number of digits in an input
    array element.

    :param list(int) A: Array of positive integers.
    """
    # sum_map stores the value of the maximum array element with a sum of
    # digits equal to sum_map[i].
    # Each array element is <= 1e9 so the sum of digits is <= 9 * 9.
    # We could use a dictionary if there's no upper bound on array elements.
    sum_map = [0] * 82

    result = -1
    for n in A:
        s = 0
        i = n
        while i > 0:
            s += i % 10
            i //= 10
        if sum_map[s] != 0:
            result = max(result, sum_map[s] + n)
        else:
            sum_map[s] = n

    return result


def test1():
    assert max_pair([18, 43, 36, 13, 7]) == 54
    print("test 1 successful")


def test2():
    assert max_pair([10, 12, 19, 14]) == -1
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
