"""
leetcode 2196: Create a binary tree from descriptions.

We are given a 2D integer array A where A[i] = [parenti, childi, islefti]
indicates that parenti is the parent of childi, in a binary tree of unique
values.

If islefti == 1, childi is the left child of parenti, else if islefti == 0 then
childi is the right child of parenti.

Build the tree and return its root.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def make_tree(A):
    """
    We build the tree and keep track of nodes in a dictionary so that we can
    update nodes when needed. We add a pointer from a child to its parent, so
    that we can find the tree root.
    """
    nodes = {}
    for val, child_val, is_left in A:
        node = nodes.get(val)
        if node is None:
            node = TreeNode(val)
            nodes[val] = node
        child = nodes.get(child_val, TreeNode(child_val, parent=node))
        nodes[child_val] = child
        if is_left:
            nodes[child] = node.left
        else:
            nodes[child] = node.right
    node = nodes.get(A[0][0])
    while node.parent:
        node = node.parent
    return node
