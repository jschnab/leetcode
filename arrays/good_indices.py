"""
leetcode 2420: find all good indices

We are given an integer array A of size n and a positive integer k.

We can an index i in the range k <= i < n - k good if the following conditions
are satisfied:

* the k elements that are just before the index i are in non-increasing order
* the k elements that are just after the index i are in non-decreasing order

Return an array of all good indices sorted in increasing order.
"""


def good_indices(A, k):
    """
    We traverse the array from left to right to count the number of elements
    before each index that are in non-increasing order, then traverse the array
    from right to left to count the number of elements after each index that
    are in non-decreasing order.

    At each index i, the 'good index' conditions are satisfied if both after[i]
    and before[i] are greater than k.

    Time complexity: O(n).
    Space complexity: O(n).
    """
    before = [1, 1]  # count elements before i in non-increasing order
    for i in range(2, len(A)):
        if A[i - 1] <= A[i - 2]:
            before.append(before[-1] + 1)
        else:
            before.append(1)

    after = [1, 1]  # count element after i in non-decreasing order
    for i in reversed(range(len(A) - 2)):
        if A[i + 1] <= A[i + 2]:
            after.append(after[-1] + 1)
        else:
            after.append(1)
    after = after[::-1]

    result = []
    for i in range(k, len(A) - k):
        if min(before[i], after[i]) >= k:
            result.append(i)
    return result


def test1():
    assert good_indices([2, 1, 1, 1, 3, 4, 1], 2) == [2, 3]
    print("test 1 successful")


def test2():
    assert good_indices([2, 1, 1, 2], 2) == []
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
