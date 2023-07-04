"""
leetcode 2570: merge two 2D arrays by summing values

We are given two 2D integer arrays A and B. A[i] = [id, val] indicate that the
number with identifier id has a value equal to val. Same for B elements.

Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id,
respecting the following conditions:

* Only ids that appear in a least one of A and B should be included in the
  resulting array.

* Each id should be included only once and its value should be the sum of the
  values of this id in the two arrays.

Return the resulting array. The returned array must be sorted in ascending
order by id.
"""


def merge(A, B):
    result = []
    i = j = 0
    while i < len(A) or j < len(B):
        # maximum id is 1000
        ida = idb = 1001
        if i < len(A):
            ida = A[i][0]
        if j < len(B):
            idb = B[j][0]
        new_id = min(ida, idb)
        new_val = 0
        if ida == new_id:
            new_val += A[i][1]
            i += 1
        if idb == new_id:
            new_val += B[j][1]
            j += 1
        result.append([new_id, new_val])
    return result


def test1():
    A = [[1, 2], [2, 3], [4, 5]]
    B = [[1, 4], [3, 2], [4, 1]]
    assert merge(A, B) == [[1, 6], [2, 3], [3, 2], [4, 6]]
    print("test 1 successful")


def test2():
    A = [[2, 4], [3, 6], [5, 5]]
    B = [[1, 3], [4, 3]]
    assert merge(A, B) == [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]
    print("test 2 successful")


if __name__ == "__main__":
    test1()
    test2()
