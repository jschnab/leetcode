"""
leetcode 2295: replace elements in an array

We are given an array A containing distrinct positive integers. We apply m
operations to this array, where in the ith operations we replace the number
operations[i][0] with operations[i][1].

It is guaranteed that in the ith operation:
- operations[i][0] exists in A
- operations[i][1] does not exist in A

Return the array after applying all operations.
"""


def replace(A, operations):
    value_to_index = {n: i for i, n in enumerate(A)}
    for i, j in operations:
        A[value_to_index[i]] = j
        value_to_index[j] = value_to_index[i]
    return A


def test1():
    assert replace([1, 2, 4, 6], [[1, 3], [4, 7], [6, 1]]) == [3, 2, 7, 1]
    print("test 1 successful")


def test2():
    assert replace([1, 2], [[1, 3], [2, 1], [3, 2]]) == [2, 1]
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
