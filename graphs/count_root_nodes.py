"""
leetcode 2581: count number of possible root nodes

Alice has an undirected tree with n nodes labeled from 0 to n-1. The tree is
represented as a 2D integer array E (edges) of length n-1 where E[i] = [a, b]
indicates there is an edge between nodes a and b.

Alice wants Bob to find the root of the tree. She allows Bob to make several
guesses about her tree. In one guess he does the following:

* Choose two distinct integers u and v such that there exists and edge [u, v]
  in the tree.

* He tells Alice that u is the parent of v in the tree.

Bob's guesses are represented by a 2D integer array G where G[i] = [u, v].

Alice does not reply to each of Bob's guesses, but just says that at least k of
his guesses are true.

Given the 2D integer arrays E and G, and the integer k, return the number of
possible nodes that can be the root of Alice's tree. If there is no such tree,
return 0.
"""

from collections import defaultdict


def brute_force(E, G, k):
    """
    We first build an undirected graph from E as an adjacency list. Considering
    each node as a potential root, we build a tree from each node as an
    adjacency set (later allowing us to quickly check parent/child
    relationships). For each tree, we check how many guesses are correct and
    count how many times k or more gusses are correct.

    Building the undirected graph takes O(len(E)) time. Iterating through nodes,
    building the tree and checking guesses takes O(n * (len(E) + len(G))). The
    total time complexity is O(n * len(E)). Space complexity is O(len(E)).
    """
    undir_graph = defaultdict(list)
    n = 0  # number of nodes in tree
    for src, dst in E:
        n = max(n, src, dst)
        undir_graph[src].append(dst)
        undir_graph[dst].append(src)

    result = 0
    for root in range(n + 1):
        dir_graph = defaultdict(set)
        stack = [root]
        while stack != []:
            cur = stack.pop()
            for child in undir_graph.get(cur, []):
                if child not in dir_graph:
                    dir_graph[cur].add(child)
                    stack.append(child)
        correct = 0
        for u, v in G:
            if v in dir_graph[u]:
                correct += 1
        if correct >= k:
            result += 1
    return result


def better(E, G, k):
    """
    We first build an undirected graph from the given edges.
    Instead of building a candidate tree for each node, we recursively traverse
    the undirected graph in a depth-first search manner to count how many
    guesses are correct. We memoize the count of correct guesses to avoid
    duplicate counting when we traverse the same edges more than once.
    """
    graph = defaultdict(list)
    for u, v in E:
        graph[u].append(v)
        graph[v].append(u)

    guess_set = set((u, v) for u, v in G)

    def correct_guesses(vertex, parent, memo):
        if (vertex, parent) in memo:
            return memo[(vertex, parent)]
        count = 0
        for child in graph[vertex]:
            if child == parent:
                continue
            if (vertex, child) in guess_set:
                count += 1
            memo[(child, vertex)] = correct_guesses(child, vertex, memo)
            count += memo[(child, vertex)]
        return count

    result = 0
    memo = {}
    for vertex in graph:
        if correct_guesses(vertex, None, memo) >= k:
            result += 1
    return result


def test1():
    E = [[0, 1], [1, 2], [1, 3], [4, 2]]
    G = [[1, 3], [0, 1], [1, 0], [2, 4]]
    assert brute_force(E, G, 3) == 3
    assert better(E, G, 3) == 3
    print("test 1 successful")


def test2():
    E = [[0, 1], [1, 2], [2, 3], [3, 4]]
    G = [[1, 0], [3, 4], [2, 1], [3, 2]]
    assert brute_force(E, G, 1) == 5
    assert better(E, G, 1) == 5
    print("test 2 successful")


if __name__ == "__main__":
    test1()
    test2()
