"""
leetcode 2208: Minimum operations to halve array sum.

We are given an array A of positive integers. In one operation we can choose
any number from A and reduce it to half its value.

Calculate the minimum number of operations to reduce the sum of the original
array by at least half its value.
"""

import heapq


def halve_array(A):
    """
    We need to always halve the value of the highest array number for each
    operation. We need to keep the array sorted after each operation, because
    the order of array items may change as we reduce them.

    This is a good use case for a heap.
    """
    s = sum(A)
    half = s / 2

    # heapq works works with a mean heap, so we take the negative of each array
    # element
    A = list(map(lambda x: -x, A))
    heapq.heapify(A)

    steps = 0
    while s > half:
        top = -1 * heapq.heappop(A)
        top /= 2
        s -= top
        heapq.heappush(A, -top)
        steps += 1

    return steps


def test1():
    assert halve_array([5, 19, 8, 1]) == 3
    print("test 1 successful")


def test2():
    assert halve_array([3, 8, 20]) == 3
    print("test 2 successful")


def test3():
    assert halve_array([1]) == 1
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
