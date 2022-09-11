"""
leetcode 2368: reachabe nodes with restrictions

There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1
edges.

We are given a 2D integer array E (edges) of length n - 1 where E[i] = [a, b]
indicates there is an edge between nodes a and b. We are also given an integer
array R (restricted) that represents restricted nodes.

Return the maximum number of nodes we can reach from node 0 without visiting a
restricted node.
"""


def reachable(n, E, R):
    restricted = set(R)
    adjacent = {i: [] for i in range(n)}
    for src, dst in E:
        adjacent[src].append(dst)
        adjacent[dst].append(src)
    seen = set()
    stack = [0]
    while stack:
        cur = stack.pop()
        for child in adjacent[cur]:
            if child not in seen and child not in restricted:
                stack.append(child)
            seen.add(cur)
    return len(seen)


def test1():
    E = [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]]
    R = [4, 5]
    assert reachable(7, E, R) == 4
    print("test 1 successful")


def test2():
    E = [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]]
    R = [4, 2, 1]
    assert reachable(7, E, R) == 3
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
