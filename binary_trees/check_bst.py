# check if a binary tree is a binary search tree


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check_bst(root):
    """
    Check if a binary tree is a binary search tree.

    :param TreeNode root: root of the tree
    :returns (bool): True if the tree is a binary search tree else False
    """
    if root:
        if root.left and (root.val < root.left.val):
            return False
        if root.right and (root.val > root.right.val):
            return False
        return check_bst(root.left) and check_bst(root.right)
    return True


def test1():
    root = None
    assert check_bst(root) is True
    print("test 1 successful")


def test2():
    root = TreeNode(3)
    assert check_bst(root) is True
    print("test 2 successful")


def test3():
    root = TreeNode(3, TreeNode(1), TreeNode(4))
    assert check_bst(root) is True
    print("test 3 successful")


def test4():
    root = TreeNode(
        4,
        TreeNode(
            2,
            TreeNode(1),
            TreeNode(3)
        ),
        TreeNode(
            6,
            TreeNode(7),
            TreeNode(8)
        )
    )
    assert check_bst(root) is False
    print("test 4 successful")


def test5():
    root = TreeNode(
        4,
        TreeNode(
            2,
            TreeNode(1),
            TreeNode(0)
        ),
        TreeNode(
            6,
            TreeNode(5),
            TreeNode(7)
        )
    )
    assert check_bst(root) is False
    print("test 5 successful")


def main():
    test1()
    test2()
    test3()
    test4()
    test5()


if __name__ == "__main__":
    main()
