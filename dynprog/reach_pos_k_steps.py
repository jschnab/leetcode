"""
leetcode 2400: number of ways to reach a position after exactly k steps.

We are given two positive integers start and end. Initially, we are standing at
position start on an infinite number line. With one step, we can move either
one position to the left, or one position to the right.

Given a positive integer k, return the number of different ways to reach the
position end, starting from start, such that we perform exactly k steps. Since
the answer may be very large, we return it modulo 10^9 + 7.

Two ways are considered different if the order of the steps made is not exactly
the same.

Note that the number line includes negative integers.
"""


def nways(start, end, k):
    if abs(start - end) > k:
        return False

    # If number of steps is odd, we can reach end only if distance between
    # start and end is odd.
    if k & 1:
        if not abs(start - end) & 1:
            return 0
    # If number of steps is even, we can reach end only if distance between
    # start and end is even.
    else:
        if abs(start - end) & 1:
            return 0

    mod = 1000000007
    memo = {}

    def helper(position, steps):
        """
        Helper function to recursively solve the problem.

        :param int position: Current position.
        :param int steps: Number of steps we can take.
        :returns (int): Number of ways we can reach end from position.
        """
        if (position, steps) in memo:
            return memo[(position, steps)]

        # If there are no more remaining steps, check if we reached the end.
        if steps == 0:
            return position == end

        # Take one step to the left
        c1 = helper(position - 1, steps - 1)

        # Take one step to the right
        c2 = helper(position + 1, steps - 1)

        memo[(position, steps)] = c1 + c2
        return (c1 + c2) % mod

    return helper(start, k)


def test1():
    assert nways(1, 2, 3) == 3
    print("test successful")


def test2():
    assert nways(2, 5, 10) == 0
    print("test successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
