"""
leetcode 2335: minimum amount of time to fill cups

We have a water dispenser that can dispense cold, warm, and hot water. Every
second, we can either fill up 2 cups with difference types of water, or 1 cup
or any type of water.

We are given an integer array 'amount' of length 3 where amount[0] is the
amount of cold water, amount[1] warm, and amount[2] hot water.

Return the minimum number of seconds needed to fill up all the cups.
"""

import heapq


def fill_cups(amount):
    amount = list(map(lambda x: -x, amount))
    heapq.heapify(amount)
    time = 0
    while -sum(amount) > 0:
        a = -heapq.heappop(amount)
        b = -heapq.heappop(amount)
        if a:
            heapq.heappush(amount, -a + 1)
            if b:
                heapq.heappush(amount, -b + 1)
            else:
                heapq.heappush(amount, -b)
        else:
            heapq.heappush(amount, -a)
            heapq.heappush(amount, -b)
        time += 1
    return time


def test1():
    assert fill_cups([1, 4, 2]) == 4
    print("test 1 successful")


def test2():
    assert fill_cups([5, 4, 4]) == 7
    print("test 2 successful")


def test3():
    assert fill_cups([5, 0, 0]) == 5
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
