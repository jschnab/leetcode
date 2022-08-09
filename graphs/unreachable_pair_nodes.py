"""
leetcode 2310: count unreachable pair of nodes in undirected graph

We are given an integer n. There is an undirected graph with n nodes, numbered
from 0 to n-1. We are given a 2D integer array 'edges' where edges[i] = (a, b),
denotes there exists an undirected edge connecting nodes a and b.

Return the number of pairs of different nodes that are unreachable from each
other.
"""

from collections import Counter


def find_parent(a, parents):
    """
    Finds the representative of each set and compress the path from a node to
    the representative of its set.

    :param int a: Node.
    :param list(int) parents: Representatives of each set.
    :returns (int): Representative of the set of a.
    """
    if parents[a] != a:
        parents[a] = find_parent(parents[a], parents)
    return parents[a]


def unreachable(n, edges):
    """
    Count unreachable pair of nodes.

    We use disjoint sets with ranks heuristics and path compression.

    1. Make n set, each initially containing one of the nodes.
    2. Find connected components.
    3. Make sure all paths are compressed.
    4. Iterate through sets and multiply their sizes to calculate the number
       of un-connected nodes.

    :param int n: Number of nodes.
    :param list(list(int)) edges: Edges.
    :returns (int): Count of unreachable pair of nodes.
    """
    # if there's no edges, none of the nodes are connected so the solution is
    # an arithmetic series over the number of nodes
    if edges == []:
        return n * (n - 1) // 2

    # 1. make n disjoint sets
    # 'parents' stores the representative element of each disjoint set
    parents = [i for i in range(n)]

    # 'ranks' stores the rank of each set, useful for the rank heuristics
    # when finding connected components
    ranks = [1 for i in range(n)]

    # 2. find connected components using path compression and ranks heuristics
    for a, b in edges:
        pa = find_parent(a, parents)
        pb = find_parent(b, parents)
        if ranks[pa] < ranks[pb]:
            parents[pa] = pb
        else:
            parents[pb] = pa
            if ranks[pa] == ranks[pb]:
                ranks[pa] += 1

    # 3. make sure all paths are compressed
    for node in range(n):
        find_parent(node, parents)

    # 4. count the pair of un-connected nodes
    result = 0
    counts = list(Counter(parents).values())
    for i in range(1, len(counts)):
        result += counts[0] * counts[i]
        counts[0] += counts[i]

    return result


def test1():
    assert unreachable(3, [[0, 1], [0, 2], [1, 2]]) == 0
    print("test 1 successful")


def test2():
    assert unreachable(7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]) == 14
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
