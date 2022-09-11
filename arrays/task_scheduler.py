"""
leetcode 2365: task scheduler II

We are given an array of positive integers T (tasks), representing tasks that
need to be completed in order, where T[i] represents the type of the ith task.

We are also given a positive integer S (space), representing the minimum number
of days that must pass after the completion of a task before another task of
the same type can be performed.

Each day, until all task have been completed, we must either:

* complete the next task from T, or
* take a break

Return the minimum number of days needed to complete all tasks.
"""
from collections import defaultdict


def schedule(T, S):
    wait = defaultdict(int)
    day = 0
    for typ in T:
        day += 1
        if wait[typ] >= day:
            day += wait[typ] - day + 1
        wait[typ] = day + S
    return day


def test1():
    assert schedule([1, 2, 1, 2, 3, 1], 3) == 9
    print("test 1 successful")


def test2():
    assert schedule([5, 8, 8, 5], 2) == 6
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
