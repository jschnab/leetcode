"""
leetcode 2508: add edges to make degrees of all nodes even

There is an undirected graph consisting of n nodes numbered from 1 to n. We are
given the integer n and a 2D array E (edges) where E[i] = [ai, bi] indicates
that there is an edgee between nodes ai and bi. The graph can be disconnected.

We can add at most two additional edges (possibly non) to this graph so that
there are no repeated edges and no self-loops.

Return True if it is possible to make the degree of each node in the graph
even, otherwise return False.

The degree of a node is the number of edges connected to it.
"""
from collections import defaultdict


def is_possible(n, edges):
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    odd_degree = []
    for i in range(1, n + 1):
        if len(graph[i]) & 1:
            odd_degree.append(i)

    if len(odd_degree) > 4 or len(odd_degree) & 1:
        return False

    if len(odd_degree) == 2:
        return any(
            [
                odd_degree[0] not in graph[odd_degree[1]],
                set(range(1, n + 1))
                - set(odd_degree)
                - graph[odd_degree[0]]
                - graph[odd_degree[1]]
                != set(),
            ]
        )

    if len(odd_degree) == 4:
        return any(
            [
                odd_degree[0] not in graph[odd_degree[1]]
                and odd_degree[2] not in graph[odd_degree[3]],
                odd_degree[0] not in graph[odd_degree[2]]
                and odd_degree[1] not in graph[odd_degree[3]],
                odd_degree[0] not in graph[odd_degree[3]]
                and odd_degree[1] not in graph[odd_degree[2]],
            ]
        )

    return True


def test1():
    n = 5
    edges = [[1, 2], [2, 3], [3, 4], [4, 2], [1, 4], [2, 5]]
    assert is_possible(n, edges) is True
    print("test 1 successful")


def test2():
    n = 4
    edges = [[1, 2], [3, 4]]
    assert is_possible(n, edges) is True
    print("test 2 successful")


def test3():
    n = 4
    edges = [[1, 2], [1, 3], [1, 4]]
    assert is_possible(n, edges) is False
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
