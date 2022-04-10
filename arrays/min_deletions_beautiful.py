"""
leetcode 2216: Minimum deletions to make array beautiful.

Given an array A, the array is beautiful if:

- the length of A is even
- A[i] != A[i + 1] for all even i

An empty array is considered beautiful.

We can delete any number of elements from A. When we deleted an element, all
elements to the right of the deleted element are shifted left to fill the gap.
All elements to the left of the deleted element remain unchanged.

Return the minimum number of elements to delete from A to make it beautiful.
"""


def min_del(A):
    """
    We use one pointer to iterate over even indices, while we keep track of
    how many deletions we had to make. We have to make a deletion when two
    elements in a pair are equal and the first index of the pair is even.

    :param list[int] A: Array to be made beautiful.
    :returns (int): Number of deletions necessary to make array beautiful.
    """
    i = j = result = 0
    while i - j + 1 < len(A):
        if A[i - j] == A[i - j + 1]:
            result += 1
            j += 1
        i += 2
    return j + (len(A) - j) % 2


def test1():
    assert min_del([1, 1, 2, 3, 5]) == 1
    print("test 1 successful")


def test2():
    assert min_del([1, 1, 2, 3]) == 2
    print("test 2 successful")


def test3():
    assert min_del([1, 1, 2, 2, 3, 3]) == 2
    # [1, 2, 2, 3] is beautiful
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
