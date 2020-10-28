# leetcode challenge 783: minimum distance between BST nodes
# given a binary search tree, return the minimum difference between the
# values of any two different nodes in the tree

# input:  [4,2,6,1,3,null,null]
# output: 1


def min_diff(root):
    """
    Traverse the tree inorder and keep track of the current node and the
    previous node, to calculate their difference.
    """
    prev = None
    node = root
    stack = []
    mini = float("inf")

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if prev is not None:
                mini = min(mini, node.val - prev.val)
            prev = node
            node = node.right

    return mini
