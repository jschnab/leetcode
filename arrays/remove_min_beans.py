"""
leetcode 2171: Removing minimum number of beans

Given an array of positive integers, where each integer represents
the number of beans in a particular bag.

We remove any number of beans from each bag (possibly 0) such that the number
of beans in each remaining non-empty bag is equal. Once a bean has been removed
from a bag it cannot be put back into a bag.

Determine the minimum number of beans we have to remove.
"""


def remove_beans(A):
    """
    If we choose to make x bags of beans empty, we should choose the x bags
    with the least amount of beans, so we first need to sort the array.

    Then, the best way to make all bags have an equal amount is to reduce all
    bags to have the same number of beans as the smallest bag.

    We iterate over how many bags we make empty and determine the minimum total
    amount of beans removed.

    Time complexity: sorting is O(nlogn) and the subsequent iteration is O(n)
    with n the array length, so the overall time complexity is O(nlogn).
    """
    A.sort()
    s = sum(A)
    length = len(A)

    # worst case, we make all bags the same size as the smallest
    result = s - length * A[0]

    # number of beans removed by emptying bags
    sum_empty_bags = 0

    for i in range(1, length):
        # make the previous bag empty...
        sum_empty_bags += A[i - 1]
        # ...and make all other bags have the same size as the smallest, which
        # is the current
        result = min(
            result,
            # (1) all removed beans so far, (2) all remaining beans in
            # bags with index > i, (3) number of beans if all bags with index
            # > i have the same size as bag i
            sum_empty_bags
            + (s - sum_empty_bags - A[i])
            - A[i] * (length - i - 1),
        )

    return result


def test1():
    assert remove_beans([4, 1, 6, 5]) == 4
    print("test 1 successful")


def test2():
    assert remove_beans([2, 10, 3, 2]) == 7
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
