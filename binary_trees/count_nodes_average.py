"""
leetcode 2265

Given the root of a binary tree, return the number of nodes where the value of
the node is equal to the average of the values in its subtree.

The average of n elements is the sum of the n elements divided by n and
rounded down to the nearest integer.

A subtree of root is a tree consisting of root and all of its descendants.
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_nodes(root):
    count = 0

    def dfs(root):
        nonlocal count
        if root:
            n_left, val_left = dfs(root.left)
            n_right, val_right = dfs(root.right)
            n = n_left + n_right + 1
            val = val_left + val_right + root.val
            if val // n == root.val:
                count += 1
            return n, val
        return 0, 0

    dfs(root)
    return count


def test1():
    root = Node(
        4,
        Node(
            8,
            Node(0),
            Node(1)
        ),
        Node(
            5,
            None,
            Node(6)
        )
    )
    assert count_nodes(root) == 5
    print("test 1 successful")


def test2():
    root = Node(1)
    assert count_nodes(root) == 1
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
