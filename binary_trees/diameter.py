"""
leetcode 543: diameter of binary tree

Given the root of a binary tree, return the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes. This path may or may not pass through the root.

The length of a path between two nodes is the number of edges between them.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter(root):
    def helper(root):
        nonlocal result
        if root is None:
            return 0
        left = helper(root.left)
        right = helper(root.right)
        result = max(result, left + right)
        return 1 + max(left, right)

    result = 0
    helper(root)
    return result


def test1():
    t = Node(1, Node(2, Node(4), Node(5)), Node(3))
    assert diameter(t) == 3
    print("test 1 successful")


def test2():
    t = Node(1, Node(2))
    assert diameter(t) == 1
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
