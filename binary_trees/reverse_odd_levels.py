"""
leetcode 2415: reverse odd levels of binary tree

Given the root of a perfect binary tree, reverse the node values at each odd
level of the tree.

It is not enough to reverse children of a node, the whole width of the tree
needs to be reversed.

Return the root of the reversed tree.

A binary tree is perfects if all parent nodes have two children and all lieaves
are on the same level.

The level of a node is the number of edges along the path between it and the
root node.
"""
from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def reverse(q):
    i = 0
    j = len(q) - 1
    while i < j:
        tmp = q[i].val
        q[i].val = q[j].val
        q[j].val = tmp
        i += 1
        j -= 1


def reverse_levels(root):
    q = deque([root])
    odd = False
    while q:
        if odd:
            reverse(q)
        for _ in range(len(q)):
            cur = q.pop()
            if cur.right:
                q.appendleft(cur.right)
            if cur.left:
                q.appendleft(cur.left)
        odd = not odd
    return root


def preorder(root):
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


def test1():
    root = Node(2, Node(3, Node(8), Node(13)), Node(5, Node(21), Node(34)))
    result = reverse_levels(root)
    assert preorder(result) == [2, 5, 8, 13, 3, 21, 34]
    print("test 1 successful")


def test2():
    root = Node(7, Node(13), Node(11))
    result = reverse_levels(root)
    assert preorder(result) == [7, 11, 13]
    print("test 2 successful")


def test3():
    root = Node(
        0,
        Node(
            1,
            Node(
                0,
                Node(1),
                Node(2)
            ),
            Node(
                0,
                Node(3),
                Node(4)
            )
        ),
        Node(
            2,
            Node(
                0,
                Node(5),
                Node(6)
            ),
            Node(
                0,
                Node(7),
                Node(8)
            ),
        )
    )
    result = reverse_levels(root)
    assert preorder(result) == [0, 2, 0, 8, 7, 0, 6, 5, 1, 0, 4, 3, 0, 2, 1]
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
