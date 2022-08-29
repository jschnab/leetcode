"""
leetcode 2349: design a number container system

Design a number container system that can do the following:

* insert of replace a number at the given index in the system
* return the smallest index for the given number in the system

Implement the NumberContainers class:

* NumberContainers() initializes the container system
* void change(int index, int number) fills the container at index with the
number.
* int find(int number) returns the smallest index for the given number, or -1
if there is no index that is filled by number in the system.
"""

import heapq
from collections import defaultdict


class NumberContainer:

    def __init__(self):
        # Store the number at each occupied index. We do not keep track of
        # unoccupied indexes.
        self.idx_to_n = {}

        # Keys are stored numbers and values are min-heap of indexes, so that
        # we can efficiently return the minimum index for a number.
        self.n_to_idx_min = defaultdict(list)

        # When updating an index, we don't update the heap of indexes. Instead,
        # we map each stored number to the set of indexes it occupies, so that
        # we can update the heap lazily: when we retrieve the minimum index
        # from the heap, we check it's still in the set of current indexes.
        self.n_to_idx_set = defaultdict(set)

    def change(self, index, number):
        n = self.idx_to_n.get(index)
        if n is not None:
            self.n_to_idx_set[n].discard(index)
        self.idx_to_n[index] = number
        self.n_to_idx_set[number].add(index)
        heapq.heappush(self.n_to_idx_min[number], index)

    def find(self, number):
        if self.n_to_idx_min[number] == []:
            return -1
        while (
            self.n_to_idx_min[number] != []
            and self.n_to_idx_min[number][0] not in self.n_to_idx_set[number]
        ):
            heapq.heappop(self.n_to_idx_min[number])
        if self.n_to_idx_min[number] != []:
            return self.n_to_idx_min[number][0]
        return -1
