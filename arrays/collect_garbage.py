"""
leetcode 2391: minimum amount of time to collect garbage

We are given an array of strings G (garbage) where G[i] represents the
assortment of garbage at the ith house. G[i] consists only of characters 'M'
(metal), 'P' (paper), and 'G' (glass). Picking up one unit of any type of
garbage takes 1 minute.

We are also given an integer array T (travel) where T[i] is the number of
minutes needed to go from house i to house i + 1.

There are three garbage trucks in the city, each responsible for picking up one
type of garbage. Each garbage truck starts at house 0 and must visit each house
in order. Trucks do not need to visit each house (if they know the remaining
houses do not have garbage to dispose of).

There is only one truck driver in the city, so only one garbage truck may be
used at any given moment. While one truck is driving or picking up garbage, the
other two trucks cannot do anything.

Return the minimum number of minutes needed to pick up all the garbage.
"""
import itertools


def collect_garbage(G, T):
    """
    We determine the last house to visit for each garbage type, we do not need
    to drive beyond this one.

    We sum up the number of garbage items to pick up, as well as the total time
    to drive to the last house, for each garbage type.
    """
    last_house = {c: i for i, g in enumerate(G) for c in g}

    # prefix sum of travel times
    # travel between houses, so there's no travel time given for the first
    # house and we need to add the initial item of the array
    dist = [0] + list(itertools.accumulate(T))

    return sum(map(len, G)) + sum(dist[last_house.get(c, 0)] for c in "PGM")


def test1():
    assert collect_garbage(["G", "P", "GP", "GG"], [2, 4, 3]) == 21
    print("test 1 successful")


def test2():
    assert collect_garbage(["MMM", "PGM", "GP"], [3, 10]) == 37
    print("test 2 successful")


def test3():
    assert collect_garbage(["PGGMG", "P", "PGPGMPPGMM"], [5, 5]) == 46
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
