"""
leetcode 2438: range product queries of powers

Given a positive integer n, there exists an array called 'powers' composed of
the minimum number of powers of 2 that sum to n. The array is sorted in
non-decreasing order, and there is only one way to form the array.

We are also given a 2D integer array 'queries' where queries[i] = [left,
right]. Each queries[i] represents a query where you have to find the product
of all powers[j] with left <= j <= right.

Return an array 'answers' equal in length to queries, where answers[i] is the
answer to the ith query. Since the answer to the ith query may be too large,
each answers[i] should be returned modulo 1e9 + 7.
"""


def run_query(left, right, p, memo):
    """
    This function recursively solves a query and memoizes results.
    """
    if left == right:
        return p[left]
    if (left, right) in memo:
        return memo[(left, right)]
    memo[(left, right)] = p[left] * run_query(left + 1, right, p, memo)
    return memo[(left, right)]


def product_queries(n, queries):
    """
    First, we calculate the decomposition of n into powers of 2, which is
    simply done by going through n bit by bit up to bith 29 (2 ** 29 is the
    first power of 2 greater than 1,000,000,000, the max value of n).

    Then we solve the problem recursively using memoization, to avoid
    recomputing the same results several times.
    """
    powers = [1 << p for p in range(30) if (1 << p) & n]
    memo = {}
    return [run_query(q[0], q[1], powers, memo) % 1000000007 for q in queries]


def test1():
    assert product_queries(15, [[0, 1], [2, 2], [0, 3]]) == [2, 4, 64]
    print("test 1 successful")


def test2():
    assert product_queries(2, [[0, 0]]) == [2]
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
