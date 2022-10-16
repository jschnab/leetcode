"""
leetcode 2405: divide intervals into minimum number of groups

We are given a 2D array 'intervals' where intervals[i] = [left, right]
represents the inclusive interval [left, right].

We have to divide the intervals into groups such that each interval is in
exactly one group, and no two intervals that are in the same group intersect
each other.

Return the minimum number of groups we need to make.

Two intervals intersect if therre is at least one common number between them.
For example, the intervals [1, 5] and [5, 8] intersect.
"""
import heapq


def group(intervals):
    """
    We sort intervals in non-decreasing order.
    We keep the right boundary of each group in a min-heap. We iterate through
    intervals, if left is greater than the smallest right boundary across
    groups, then we can add the current interval to this group. Otherwise, we
    need to create a new group.
    """
    groups = []
    for left, right in sorted(intervals):
        if groups and left > groups[0]:
            # update the right boundary of the group
            heapq.heappop(groups)
        # if heap was popped, this is an update, else this is creating a group
        heapq.heappush(groups, right)
    return len(groups)


def test1():
    intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
    assert group(intervals) == 3
    print("test 1 successful")


def test2():
    intervals = [[1, 3], [5, 6], [8, 10], [11, 13]]
    assert group(intervals) == 1
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
