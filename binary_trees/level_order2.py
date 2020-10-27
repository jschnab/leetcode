from collections import deque

# leetcode challenge 107: binary tree level order traversal II
# given a binary tree, return the bottom-up level order traversal of its
# nodes values (left to right, level by level from leaf to root)

# input:  [3,9,20,null,null,15,7]
# output: [[15,7],[9,20],[3]]

def level_order(root):
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if not root:
        return []

    result = []
    q = deque([root])

    # iterative breadth-first search
    while q:
        level = []
        for _ in range(len(q)):
            node = q.pop()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)

    # bottom-up order
    return result[::-1]
