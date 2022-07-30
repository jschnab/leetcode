"""
leetcode 2305: fair distribution of cookies

You are given an integer array 'cookies' where cookies[i] denotes the number of
cookies in the ith bag. You are also given an integer k that denotes the number
of children to distribute all the bags of cookies to. All the cookies in the
same bag must go the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies
obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.
"""


def min_unfair(cookies, k):
    """
    We recursively explore all possible distributions: for every child we
    choose to give or not give a given bag of cookies.

    Once we recursed N times (with N number bag of cookies), there are no more
    cookies to distribute and we update result, which is the minimum of all
    unfair cookie distributions (i.e. the maximum number of cookies distributed
    to a single child in a given distribution).

    Time complexity: O(k^n) where n is the number of cookie bags. The depth of
    recursion is n, and at each recursion level we iterate through k children.
    """
    distri = [0] * k
    result = float("inf")

    def helper(cookies, distri, k, level):
        nonlocal result
        if level == len(cookies):
            result = min(result, max(distri))
        else:
            for i in range(k):
                distri[i] += cookies[level]
                helper(cookies, distri, k, level + 1)
                distri[i] -= cookies[level]

                # prune the recursion tree, otherwise we calculate the same
                # distribution (with different children) several times
                if distri[i] == 0:
                    break

    helper(cookies, distri, k, 0)
    return result


def test1():
    assert min_unfair([8, 15, 10, 20, 8], 2) == 31
    print("test 1 successful")


def test2():
    assert min_unfair([6, 1, 3, 2, 2, 4, 1, 2], 3) == 7
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
