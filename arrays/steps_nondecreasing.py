"""
leetcode 2289: steps to make array non-decreasing

We are given an integer array A. In one step, we remove all elements A[i] where
A[i - 1] > A[i] for all 0 < i < length(A).

Return the number of steps performed until A becomes a non-decreasing array.
"""


def steps(A):
    """
    Since we need to know how many smaller array elements follow a given
    element, we iterate through the array in reverse order, so that we can
    iterate through the array only once.

    We keep a stack of array indexes pointing to non-decreasing array elements.
    The last element of the stack is the last visited array element when
    iterating.

    We also keep an table containing the number of smaller and monotonously
    decreasing array elements that follow a given array element. For example,
    if indices 3, 4, 5 of the array a monotonously decreasing and smaller than
    index 2, then table[0] = 3.

    We also keep track of the maximum value in the table. When we are done,
    this will be the solution to the problem.

    We iterate through the array in reverse order and update stack, table, and
    result. We finally return result.

    Time complexity: O(n). We always iterate once through the array. If the
    input array contains element in monotonous decreasing order, the stack
    never contains more than element and the while loop exits after one
    iteration. In short, the stack never contains more than the elements that
    are not visited yet by the outer loop, so we visit each element at most
    twice (once from the input array in the outer loop, once from the stack in
    the inner loop).

    Space complexity: O(n). At worst, we store all indices of the original
    array in the stack.
    """
    stack = []
    tab = [0] * len(A)
    result = 0
    for i in reversed(range(len(A))):
        while stack and A[i] > A[stack[-1]]:
            tab[i] = max(tab[i] + 1, tab[stack.pop()])
            result = max(result, tab[i])
        stack.append(i)
    return result


def test1():
    assert steps([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]) == 3
    print("test 1 successful")


def test2():
    assert steps([4, 5, 7, 7, 13]) == 0
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
