"""
leetcode 70: climbing stairs

We are climbing a staircase. It takes n steps to reach the top.

Each time we can either climb 1 or 2 steps. In how many distinct ways can we
climb to the top?
"""


def climb1(n):
    """
    Top-down ecursive dynamic programming solution.

    We recursively take 1 or 2 steps, starting from zero. Since we will
    encounter the same step several times, we memoize the solution using a
    dictionary.

    At every step:

    - if we overshot, then this sequence of steps is not a solution and we
      return 0
    - if we found the target then this sequence of steps is a solution and we
      return 1.
    - else we have to take more steps: we return the memoized solution if it
      exists else we recurse.
    """

    def helper(steps_taken, target, memo):
        if steps_taken in memo:
            return memo[steps_taken]
        if steps_taken > target:
            return 0
        if steps_taken == target:
            return 1
        memo[steps_taken] = helper(steps_taken + 1, target, memo) + helper(
            steps_taken + 2, target, memo
        )
        return memo[steps_taken]

    memo = {}
    return helper(0, n, memo)


def climb2(n):
    """
    We notice that the solution forms a Fibonacci sequence.
    """
    a = 0
    b = 1
    for i in range(n):
        tmp = a + b
        a = b
        b = tmp
    return b


def test1():
    assert climb1(2) == 2
    assert climb2(2) == 2
    print("test 1 successful")


def test2():
    assert climb1(3) == 3
    assert climb2(3) == 3
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
