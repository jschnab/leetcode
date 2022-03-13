"""
leetcode 2187: Minimum time to complete trips.

Given an array `T` where `T[i]` is the time taken by the ith bus to
complete one trip.

In parallel, all buses is making successive trips (after a bus completed a trip
it immediately starts a new trip).

Given an integer that indicates the number of trips all buses should make in
total, determine the minimum time required for all buses to complete at least
the total number of trips.
"""


def min_time(T, total):
    """
    We could iterate over times, and determine how many trips each bus did for
    each time, then stop iterating when we reach at least total.

    We can also do a binary search between 1 and the time it takes for the
    slowest bus to do all required trips.

    Time complexity: O(N*log(min(T)*total)) with N the length of T.
    """
    low = 1
    high = min(T) * total
    while low < high:
        mid = (low + high) // 2
        if sum(mid // t for t in T) >= total:
            high = mid
        else:
            low = mid + 1
    return low


def test1():
    assert min_time([1, 2, 3], 5) == 3
    print("test 1 successful")


def test2():
    assert min_time([2], 1) == 2
    print("test 2 successful")


def test3():
    assert min_time([5, 10, 10], 9) == 25
    print("test 3 successful")


def test4():
    assert min_time([9, 3, 10, 5], 2) == 5
    print("test 4 successful")


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
