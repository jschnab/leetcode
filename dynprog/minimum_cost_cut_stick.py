"""
leetcode 1547: minimum cost to cut a stick

Given a wooden stick of length n, the stick is labeled from 0 to n (like a
ruler).

Given an integer array 'cuts' where cuts[i] denotes a position where we should
cut the stick. We can perform the cuts in any order.

The cost of one cut is the length of the stick to be cut. The total cost is the
sum of costs to all cuts.

Return the minimum total cost of the cuts.
"""


def mini_cost(n, cuts):
    """
    """
    memo = {}
    cuts = [0] + sorted(cuts) + [n]

    def cost(left, right):
        if (left, right) in memo:
            return memo[(left, right)]

        # No more stick left to cut.
        if right - left == 1:
            return 0

        memo[(left, right)] = min(
            cost(left, i) + cost(i, right) + cuts[right] - cuts[left]
            for i in range(left + 1, right)
        )
        return memo[(left, right)]

    return cost(0, len(cuts) - 1)


def test1():
    assert mini_cost(7, [1, 3, 4, 5]) == 16
    print("test 1 successful")


def test2():
    assert mini_cost(9, [5, 6, 1, 4, 2]) == 22
    print("test 2 successful")


if __name__ == "__main__":
    test1()
    test2()
