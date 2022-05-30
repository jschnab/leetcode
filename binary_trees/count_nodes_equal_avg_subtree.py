"""
leetcode 2265: Count nodes equal to average of subtree.

Given the root of a binary tree, return the number of nodes where the value of
the node is equal to the average of the values in its subtree.

The average of n elements is the sum of the n elements divided by n and rounded
down to the nearest integer.

A subtree of root is a tree consisting of root and all of its descendents.
"""


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


def count_nodes(root):
    count = 0

    def dfs(root):
        nonlocal count
        if root:
            n_left, val_left = dfs(root.left)
            n_right, val_right = dfs(root.right)
            if (root.val + val_left + val_right) // (
                n_left + n_right + 1
            ) == root.val:
                count += 1
            return n_left + n_right + 1, val_left + val_right + root.val
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


def test3():
    root = Node(
        1,
        None,
        Node(
            3,
            None,
            Node(
                1,
                None,
                Node(3)
            )
        )
    )
    assert count_nodes(root) == 1
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
