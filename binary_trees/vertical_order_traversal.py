"""
leetcode 987: vertical order traversal of binary tree

Given the root of a binary tree, calculate the vertical order traversal of the
binary tree.

For each node at position (row, col), its left child will be at position
(row + 1, col - 1) and its right child will be at position (row + 1, col + 1).
The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom
orderings for each column index starting from the leftmost column and ending on
the rightmost column. There may be multiple nodes in the same row and same
column, in which case we sort these nodes by their values.
"""


from collections import defaultdict


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def shape(root):
    """
    Traverse a binary tree and determines the depth of the tree, the width of
    the tree, and the offset of the leftmost column compared to the root.
    """
    height, min_col, max_col = 0, 0, 0
    stack = [(root, 0, 0)]
    while stack:
        node, row, col = stack.pop()
        height = max(height, row)
        max_col = max(max_col, col)
        min_col = min(min_col, col)
        if node.left:
            stack.append((node.left, row + 1, col - 1))
        if node.right:
            stack.append((node.right, row + 1, col + 1))
    return height, max_col - min_col + 1, -min_col


def traverse(root):
    height, n_col, min_col = shape(root)

    # Every cell in the grid is a list because several nodes can occupy the
    # same cell in the grid.
    grid = [[[] for _ in range(n_col)] for _ in range(height + 1)]

    stack = [(root, 0, 0)]
    while stack:
        node, row, col = stack.pop()
        grid[row][min_col + col].append(node.val)
        if node.left:
            stack.append((node.left, row + 1, col - 1))
        if node.right:
            stack.append((node.right, row + 1, col + 1))
    result = [[] for _ in range(n_col)]
    for row in grid:
        for idx, val in enumerate(row):
            if val:
                result[idx].extend(sorted(val))
    return result


def traverse2(root):
    seen = defaultdict(lambda: defaultdict(list))

    def dfs(node, col=0, row=0):
        if node:
            seen[col][row].append(node)
            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)

    dfs(root)
    grid = []

    for col in sorted(seen):
        grid_col = []
        for row in sorted(seen[col]):
            grid_col.extend(sorted(node.val for node in seen[col][row]))
        grid.append(grid_col)

    return grid


def test1():
    t = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    assert traverse(t) == [[4], [2], [1, 5, 6], [3], [7]]
    assert traverse2(t) == [[4], [2], [1, 5, 6], [3], [7]]
    print("test 1 successful")


def test2():
    t = Node(1, Node(2, Node(4), Node(6)), Node(3, Node(5), Node(7)))
    assert traverse(t) == [[4], [2], [1, 5, 6], [3], [7]]
    assert traverse2(t) == [[4], [2], [1, 5, 6], [3], [7]]
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
