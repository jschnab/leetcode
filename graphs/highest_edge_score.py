"""
leetcode 2374: node with highest edge score

We are given a directed graph with n nodes labeled from 0 to n - 1, where each
node has exactly one outgoing edge.

The graph is represented by an integer array E of length n, where E[i]
indicates that there is a directed edge from node i to node E[i].

The edge score of a node i is defined as the sum of the labels of all the nodes
that have an edge pointing to i.

Return the node with the highest edge score. If multiple nodes have the same
edge score, return the node with the smallest index.
"""
from collections import defaultdict


def edge_score(E):
    scores = defaultdict(int)
    for src, dst in enumerate(E):
        scores[dst] += src
    return sorted(scores.items(), key=lambda x: (x[1], -x[0]))[-1][0]


def test1():
    assert edge_score([1, 0, 0, 0, 0, 7, 7, 5]) == 7
    print("test 1 successful")


def test2():
    assert edge_score([2, 0, 0, 2]) == 0
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
