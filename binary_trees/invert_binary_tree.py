# leetcode challenge 266: invert binary tree
# given a binary tree, invert the left and right subtree of every node

from collections import deque


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_recur1(root):
    """
    Invert a binary tree using recursion.

    Time complexity: O(n) each node is visited once
    Space complexity: O(h) where h is the height of the tree, because the
                      call stack is as high as the tree

    :param TreeNode root: root of the tree
    """
    if root:
        tmp = root.right
        root.right = root.left
        root.left = tmp
        invert_recur1(root.left)
        invert_recur1(root.right)


def invert_recur2(root):
    """
    Invert a binary tree using recursion.

    :param TreeNode root: root of the tree
    """
    if root:
        right = invert_recur2(root.right)
        left = invert_recur2(root.left)
        root.left = right
        root.right = left
        return root


def invert_iter(root):
    """
    Use breadth-first search to iteratively invert the tree.

    Time complexity: O(n) we visit each node once
    Space complexity: O(n), in the worst case the queue will contain all nodes
                      in one level of the tree. A full binary tree has
                      ceiling(n/2) leaves.

    :param TreeNode root: root of the tree
    """
    if root:
        q = deque([root])
        while q:
            node = q.pop()
            if node:
                q.appendleft(node.left)
                q.appendleft(node.right)
                tmp = node.left
                node.left = node.right
                node.right = tmp
