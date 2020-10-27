# leetcode challenge 530: minimum absolute difference in BST
# given a binary search tree with non-negative values, find the minimum
# absolute difference between values of any two nodes

# input:  [1,null,3,2]
# output: 1


def min_abs_diff(root):
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if not root:
        return 0

    node = root
    result = float("inf")
    stack = []
    prev = None

    # iterative inorder
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node and prev:
                result = min(result, node.val - prev.val)
            prev = node
            node = node.right

    return result
