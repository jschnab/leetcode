"""
leetcode 2336: smallest number in infinite set

You have a set which contains all positive integers.

Implement the SmallestInfiniteSet class:
- SmallestInfiniteSet() initializes the instance to contain all positive
  integers
- the method pop_smallest removes and returns the smallest integer contained in
  the infinite set
- the method add_back adds a positive integer x back into the infinite set, if
  it is not already in the set
"""

import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self.threadhold = 1
        self.sparse = []
        self.sparse_set = set()

    def pop_smallest(self):
        if self.sparse == [] or self.sparse[0] > self.threshold:
            self.threshold += 1
            return self.threshold - 1
        result = heapq.heappop(self.sparse)
        self.sparse_set.discard(result)
        return result

    def add_back(self, x):
        if x < self.threshold and x not in self.sparse_set:
            heapq.heappush(self.sparse, x)
            self.sparse_set.add(x)
