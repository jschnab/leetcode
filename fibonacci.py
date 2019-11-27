# functions to get Nth element of fibonacci sequence with different
# programming approaches

# iterative solution
# time O(n) and space O(1)
def fib_iter(n):
    """Get nth fibonacci sequence number with iterative approach."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# recursive approach
# time O(2^n) and space O(n)
def fib_recur(n):
    """Get nth fibonacci sequence number with recursive approach."""
    if n < 2:
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)

# dynamic programming approach
# time O(n) and space O(n)
def fib_dp(n):
    """Get nth fibonacci sequence number with dynamic programming approach."""
    def helper(m):
        if m < 2:
            return m
        if memo[m]:
            return memo[m]
        memo[m] = helper(m - 1) + helper(m - 2)
        return memo[m]

    memo = [0] * (n + 1)
    return helper(n)
