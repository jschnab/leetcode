"""
leetcode 2170: Minimum operations to make the array alternating

Given an array A of n positive integers, we want to make an alternating array:

* A[i - 2] == A[i], 2 <= i <= n - 1
* A[i - 1] != A[i]. 1 <= i <= n - 1

In one operation we can change the number at any position in the array
into any positive integer.

We want to determine the minimum number of operations to make the array
alternating.
"""


def alternate(A):
    """
    For odd and even array indexes, determine the top two frequent numbers.
    The array that contains a combination of either pair of these numbers is
    the array we can produce with the minimum number of changes compared to the
    input array. Of course, we want alternating numbers to be different so we
    determine the top 2 numbers for each index parity.

    Time complexity: there are three loops that iterate through array items
    with O(n), running one after the other, so the overall time complexity is
    O(n), with n the array length.
    """
    # the array is trivially alternating
    if len(A) < 2:
        return 0

    # count numbers in the array, according to index parity
    count_odd = {}
    count_even = {}
    for idx, n in enumerate(A):
        if idx & 1:
            count_odd[n] = count_odd.get(n, 0) + 1
        else:
            count_even[n] = count_even.get(n, 0) + 1

    # determine top 2 numbers based on counts
    maxi_odd = [(None, 0), (None, 0)]
    maxi_even = [(None, 0), (None, 0)]
    for n, c in count_odd.items():
        if c > maxi_odd[0][1]:
            maxi_odd[1] = maxi_odd[0]
            maxi_odd[0] = (n, c)
        elif c > maxi_odd[1][1]:
            maxi_odd[1] = (n, c)
    for n, c in count_even.items():
        if c > maxi_even[0][1]:
            maxi_even[1] = maxi_even[0]
            maxi_even[0] = (n, c)
        elif c > maxi_even[1][1]:
            maxi_even[1] = (n, c)

    # if the top 2 numbers are different we can use them to build the
    # alternating array
    if maxi_even[0][0] != maxi_odd[0][0]:
        return len(A) - maxi_even[0][1] - maxi_odd[0][1]

    # otherwise we need to use a combination of top 1 and 2 numbers
    return len(A) - max(
        maxi_odd[0][1] + maxi_even[1][1],
        maxi_odd[1][1] + maxi_even[0][1],
    )


def test1():
    A = [3, 1, 3, 2, 4, 3]
    assert alternate(A) == 3
    print("test 1 successful")


def test2():
    A = [1, 2, 2, 2, 2]
    assert alternate(A) == 2
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
