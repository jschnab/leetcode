"""
leetcode 2426: number of pairs satisfying inequality

We are given two integer arrays A and B, each of size n, and an integer diff.
Find the number of pairs (i, j) such that:

* 0 <= i < j <= n - 1
* A[i] - A[j] <= B[i] - B[j] + diff

Return the number of pairs that satisfy the conditions.

Constraints:

* 2 <= n <= 100,000
* -10,000 <= A[i], B[i] <= 10,000
* -10,000 <= diff <= 10,000
"""
from sortedcollections import SortedList


class FenwickTree:
    def __init__(self, n):
        self.items = [0] * (n + 1)

    def lsb(self, x):
        "Least significant bit of x."
        return x & -x

    def update_item(self, idx, val):
        idx += 1
        while idx < len(self.items):
            self.items[idx] += val
            idx += self.lsb(idx)

    def prefix_sum(self, idx):
        idx += 1
        result = 0
        while idx > 0:
            result += self.items[idx]
            idx -= self.lsb(idx)
        return result


def npairs_fenwick(A, B, diff):
    """
    We reorganize the problem condition into C[i] - C[j] <= diff where C[i] =
    A[i] - B[i].

    We can use a Fenwick tree (binary-indexed tree) where the indexes of tree
    items are defined by C (offset by the appropriate value to account for
    negative integers in the input). Tree item values are the number of items
    in C with the value corresponding to the tree item index. This way, we can
    calculate pairs using a prefix sum, which is done in O(lgn) in a Fenwick
    tree. The space complexity is O(n).
    """
    offset = 30000
    T = FenwickTree(offset * 2 + 1)
    result = 0
    for a, b in zip(A, B):
        result += T.prefix_sum(a - b + diff + offset)
        T.update_item(a - b + offset, 1)
    return result


def npairs_binsearch(A, B, diff):
    """
    We reorganize the problem condition into C[i] - C[j] <= diff where C[i] =
    A[i] - B[i].

    We use binary search on sorted C. Since we are looking for items lesser
    than or equal to diff, we use the right boundary of the bisection.

    We use a SortedList object from the sortedcollections library to store C.

    Time complexity: O(lgn)
    Space complexity: O(n)
    """
    L = SortedList()
    result = 0
    for a, b in zip(A, B):
        result += L.bisect_right(a - b + diff)
        L.add(a - b)
    return result


def test1():
    A = [3, 2, 5]
    B = [2, 2, 1]
    diff = 1
    assert npairs_fenwick(A, B, diff) == 3
    assert npairs_binsearch(A, B, diff) == 3
    print("test 1 successful")


def test2():
    A = [3, -1]
    B = [-2, 2]
    diff = -1
    assert npairs_fenwick(A, B, diff) == 0
    assert npairs_binsearch(A, B, diff) == 0
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
