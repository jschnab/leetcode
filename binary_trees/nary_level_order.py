"""
leetcode 429: n-ary tree level order traversal

Given an n-ary tree, return the level order traversal of its nodes' values.
"""
from collections import deque


class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children or []


def traverse(root):
    if root is None:
        return []
    result = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            cur = q.pop()
            level.append(cur.val)
            for c in cur.children:
                q.appendleft(c)
        result.append(level)
    return result


def test1():
    t = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    assert traverse(t) == [[1], [3, 2, 4], [5, 6]]
    print("test 1 successful")


def test2():
    t = Node(
        1,
        [
            Node(2),
            Node(
                3,
                [
                    Node(6),
                    Node(7, [Node(11, [Node(14)])]),
                ]
            ),
            Node(4, [Node(8, [Node(12)])]),
            Node(
                5,
                [
                    Node(9, [Node(13)]),
                    Node(10),
                ]
            ),
        ]
    )
    expected = [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]]
    assert traverse(t) == expected
    print("test 2 successful")


def test3():
    assert traverse(None) == []
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
