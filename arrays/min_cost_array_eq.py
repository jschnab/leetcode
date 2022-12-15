"""
leetcode 2448: minimum cost to make array equal

We are given two arrays nums and cost consisting each of n positive integers.

We can do the following operation any number of times:

* increase or decrease any elements of the array nums by 1

The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums
become equal.
"""


def min_cost(nums, cost):
    """
    The minimum cost is achieved by making all elements equal to the median of
    the array, weighted by the cost. To easily weight elements by their cost,
    we can make a new array where every element nums[i] is repeated cost[i]
    times. We can "simulate" the array, and find the median with binary search.
    """
    total_cost = sum(cost)
    lo = 0  # after binary search, lo equals the weighted median of nums
    hi = 1000000  # the maximum value of any element of nums
    while lo < hi:
        sum_ = 0
        mid = (lo + hi) // 2
        for i in range(len(nums)):
            if nums[i] <= mid:
                sum_ += cost[i]
        if sum_ <= total_cost // 2:
            lo = mid + 1
        else:
            hi = mid
    return sum(abs(nums[i] - lo) * cost[i] for i in range(len(nums)))


def test1():
    assert min_cost([1, 3, 5, 2], [2, 3, 1, 14]) == 8
    print("test 1 successful")


def test2():
    assert min_cost([2, 2, 2, 2, 2], [4, 2, 8, 1, 3]) == 0
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
