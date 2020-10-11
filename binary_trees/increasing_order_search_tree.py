# leetcode challenge 897: increasing search tree
# given a binary search tree, rearrange the tree in-order so that the leftmost
# node in the tree in the new root of the tree, every node has no left child
# and only one right child
# this is basically an in-order linearization of the tree


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def linearization_recur1(root):
    """
    Build a new tree by recursively traversing the old tree in order.

    Time complexity: O(n)
    Space complexity: O(n), the size of the call stack.
    """
    def helper(root):
        nonlocal new
        if root:
            helper(root.left)
            new.right = TreeNode(root.val)
            new = new.right
            helper(root.right)

    dummy = new = TreeNode()
    helper(root)
    return dummy.right


def linearization_recur2(root):
    """
    Reorganize the tree by recursively traversing it in order.

    Time complexity: O(n)
    Space complexity: O(h) where h is the height of the tree
    """
    def helper(root):
        nonlocal new
        if root:
            helper(root.left)
            root.left = None
            new.right = root
            new = new.right
            helper(root.right)

    dummy = new = TreeNode()
    helper(root)
    return dummy.right


def linearization_iter1(root):
    """
    Build a new tree by iteratively traversing the old tree in order.

    Time complexity: O(n)
    Space complexity: O(n) to store the new tree
    """
    if not root:
        return
    tree = None
    node = root
    stack = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if tree:
                tree.right = TreeNode(node.val)
                tree = tree.right
            else:
                tree = TreeNode(node.val)
                result = tree
            node = node.right
    return result


def linearization_iter2(root):
    """
    Reorganize the tree by iteratively traversing it in order.

    Time complexity: O(n)
    Space complexity: O(h) where h is the height of the tree
    """
    if not root:
        return
    node = root
    stack = []
    dummy = current = TreeNode()
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            node.left = None
            current.right = node
            current = current.right
            node = node.right
    return dummy.right


def traverse(root):
    result = []
    while root:
        result.append(root.val)
        root = root.right
    return result


def test1():
    tree = TreeNode(
        4,
        TreeNode(
            2,
            TreeNode(1),
            TreeNode(3)
        ),
        TreeNode(
            6,
            TreeNode(5),
            TreeNode(7)
        ),
    )
    result = linearization_iter1(tree)
    assert traverse(result) == [1, 2, 3, 4, 5, 6, 7]
    print("test 1 successful")


def test2():
    tree = None
    result = linearization_iter1(tree)
    assert traverse(result) == []
    print("test 2 successful")


def test3():
    tree = TreeNode(
        4,
        TreeNode(
            2,
            TreeNode(1),
            TreeNode(3)
        ),
        TreeNode(
            6,
            TreeNode(5),
            TreeNode(7)
        ),
    )
    result = linearization_iter2(tree)
    assert traverse(result) == [1, 2, 3, 4, 5, 6, 7]
    print("test 3 successful")


def test4():
    tree = TreeNode(
        4,
        TreeNode(
            2,
            TreeNode(1),
            TreeNode(3)
        ),
        TreeNode(
            6,
            TreeNode(5),
            TreeNode(7)
        ),
    )
    result = linearization_recur1(tree)
    assert traverse(result) == [1, 2, 3, 4, 5, 6, 7]
    print("test 4 successful")


def test5():
    tree = TreeNode(
        4,
        TreeNode(
            2,
            TreeNode(1),
            TreeNode(3)
        ),
        TreeNode(
            6,
            TreeNode(5),
            TreeNode(7)
        ),
    )
    result = linearization_recur2(tree)
    assert traverse(result) == [1, 2, 3, 4, 5, 6, 7]
    print("test 5 successful")


def main():
    test1()
    test2()
    test3()
    test4()
    test5()


if __name__ == "__main__":
    main()
