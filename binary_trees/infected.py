"""
leetcode 2385: amount of time for binary tree to be infected

We are given the root of a binary tree with unique values and an integer start.
At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

* the node is currently uninfected
* the node is adjacent to an infected node

Calculate the number of minutes needed for the whole tree to be infected.
"""
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def infection(root, start):
    """
    We add a parent to each node, and then we traverse the tree in every
    direction from the start, using breadth-first search.: to parent and to
    children. We calculate the maximum distance we can reach in any direction.
    """
    stack = [(root, None)]
    while stack:
        cur, par = stack.pop()
        if cur.val == start:
            start = cur
        cur.parent = par
        if cur.left:
            stack.append((cur.left, cur))
        if cur.right:
            stack.append((cur.right, cur))

    q = deque([(start, 0)])
    seen = {start}
    result = 0
    while q:
        cur, time = q.pop()
        result = max(result, time)
        for child in (cur.parent, cur.left, cur.right):
            if child and child not in seen:
                q.appendleft((child, time + 1))
                seen.add(child)

    return result


def test1():
    root = Node(
        1,
        Node(5, Node(4, Node(9), Node(2))),
        Node(3, Node(10), Node(6))
    )
    assert infection(root, 3) == 4
    print("test 1 successful")


def test2():
    root = Node(1)
    assert infection(root, 1) == 0
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
