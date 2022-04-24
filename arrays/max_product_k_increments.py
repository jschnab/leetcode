"""
We are given an array of positive integers A and an integer k. In one operation
we can choose any element from A and increment it by 1.

Return the maximum product of elements of A after at most k operations. Return
the answer modulo 1e9 + 7.
"""

import functools
import heapq


def max_product(A, k):
    """
    To maximize the product of A elements, we have to perform all k operations
    and always choose the smallest element of A for a given operation.

    A min-heap is a data structure that allows us to retrieve the smallest
    element of A in O(1) and push the incremented element back in O(lgn).

    Time complexity: O(klogn).
    Space complexity: O(1).
    """
    heapq.heapify(A)
    for _ in range(k):
        heapq.heappush(A, heapq.heappop(A) + 1)
    result = functools.reduce(lambda x, y: x * y, A) % (10 ** 9 + 7)
    return result


def test1():
    assert max_product([0, 4], 5) == 20
    print("test 1 successful")


def test2():
    assert max_product([6, 3, 3, 2], 2) == 216
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
