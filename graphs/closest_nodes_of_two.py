"""
leetcode 2359: find closest node to given two nodes

We are given a directed graph of n nodes numbered from 0 to n - 1, where each
node has at most one outgoing edge.

The graph is represented with a given index array E (edges) of size n,
indicated that there is a directed edge from node i to node edges[i]. If there
is no outgoing edge from i, then edges[i] = -1.

We are also given two integers N and M (index of nodes).

Return the index of the node that can be reached from both N and M, such that
the maximum distance from N to that node, and from M to that node is minimized.
If there are multiple answers, return the node with the smallest index, and if
no possible answer exists, return -1.

Note that the graph may contain cycles.
"""


def closest_node(E, M, N):
    """
    We first calculate the distance of M and N to each node of the graph.

    Then, amongst the nodes reachable by both M and N, we take the maximum
    distance between M-node and N-node, and return its minimum value across all
    distances.
    """
    # Record the distance of M to other nodes.
    children_m = {M: 0}
    cur = E[M]
    dist = 1
    while cur != -1 and cur not in children_m:
        children_m[cur] = dist
        dist += 1
        cur = E[cur]

    # Record the distance of N to other nodes.
    children_n = {N: 0}
    cur = E[N]
    dist = 1
    while cur != -1 and cur not in children_n:
        children_n[cur] = dist
        dist += 1
        cur = E[cur]

    result = -1
    min_dist = float("inf")
    for node in children_m:
        if node in children_n:
            max_dist = max(children_m[node], children_n[node])

            # Use the node index as a tie-break.
            if max_dist == min_dist:
                result = min(result, node)

            elif max_dist < min_dist:
                result = node
                min_dist = max_dist

    return result


def test1():
    assert closest_node([2, 2, 3, -1], 0, 1) == 2
    print("test 1 successful")


def test2():
    assert closest_node([1, 2, -1], 0, 2) == 2
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
