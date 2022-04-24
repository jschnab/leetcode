"""
Given an integer array A, where each array element indicates the size of a pile
of candies. We can divide each pile into any number of smaller piles, but we
cannot merge to piles together.

We are also given an integer k that represents the number of children. We have
to allocate piles of candies to children such that each children gets the same
number of candies (same pile size). Each children can take at most one pile of
candies and some piles of candies may end up not used.

Return the maximum number of candies each children can get.
"""


def allocate_candies(A, k):
    """
    Given a pile of candies of size s, it's easy to calculate how many
    children we could feed (lines 32-34). We could start from the
    maximum number of children we could ever feed (ignoring piles) and
    iteratively calculate how many children we can feed by splitting
    piles, decrementing the number of children by one if we cannot feed them
    all else return the first valid value.

    We can improve the time performance by using a binary search instead of
    a linear search.

    Time complexity: O(len(A) * lg(N)) with N the total number of candies.
    Space complexity: O(1).
    """
    lo = 0

    # the maximum number of candies we could theoretically allocate
    # to each children (if we ignored piles)
    hi = sum(A) // k

    while lo < hi:
        mid = (lo + hi + 1) // 2

        # n is the maximum number of children that can get a pile of candies
        # of size mid
        n = 0
        for pile in A:
            n += pile // mid

        # if we can feed more children than expected, we could give less
        # more candies to each children
        if n >= k:
            lo = mid

        # we are trying to give too many candies per children
        else:
            hi = mid - 1

    return lo


def test1():
    assert allocate_candies([5, 8, 6], 3) == 5
    print("test 1 successful")


def test2():
    assert allocate_candies([2, 5], 11) == 0
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
