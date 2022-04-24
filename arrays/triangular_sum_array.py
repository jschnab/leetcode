"""
Given an integer array A, where A[i] is between 0 and 9 (inclusive).

The triangular sum of A is the value of the only element present in A after
the following process terminates:

1 2 3 4 5
 3 5 7 9
  8 2 6
   0 8
    8

Starting with A = [1,2,3,4,5], we add each pair of adjacent elements in A
to make a new array.

Return the last element remaining, which is the triangular sum of A.
"""


def triangular_sum(A):
    """
    We simply implement the instructions and calculate the sum in place,
    by replacing each array element.

    Time complexity: We have an arithmetic series so O(n**2).
    Space complexity: We work in place so O(1).
    """
    n = len(A)
    while n > 1:
        for i in range(n - 1):
            A[i] = (A[i] + A[i + 1]) % 10
        n -= 1
    return A[0]


def pascal_triangle(A):
    """
    We note that the coefficient to apply to each element of the input array
    to arrive at the result for Pascal's triangle.

    https://en.wikipedia.org/wiki/Pascal%27s_triangle

    Pascal's triangle is made of binomial coefficient, so we can use the
    multiplicative formula to calculate these coefficients. We apply the
    coefficients to array elements to calculate the solution in a single
    array iteration.

    Starting at coefficient mCk, the next one mC(k+1) is:
    mCk * (m - k) / (k + 1)

    https://en.wikipedia.org/wiki/Binomial_coefficient#Multiplicative_formula
    """
    m = len(A) - 1  # we get coefficient from the mth level of the triangle
    mCk = 1  # initial binomial coefficient
    result = 0
    for i, n in enumerate(A):
        result = (result + mCk * n) % 10
        mCk = mCk * (m - i) // (i + 1)
    return result


def test1():
    assert triangular_sum([1, 2, 3, 4, 5]) == 8
    assert pascal_triangle([1, 2, 3, 4, 5]) == 8
    print("test 1 successful")


def test2():
    assert triangular_sum([5]) == 5
    assert pascal_triangle([5]) == 5
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
