# delete a node with a certain value from a binary search tree
# we assume all nodes have distinct values

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_list(root):
    """
    Traverse tree in order and return list of node values.

    :param TreeNode root: root of the tree
    :returns (list): list of node values, inorder
    """
    result = []
    stack = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            result.append(root.val)
            root = root.right
    return result


def find_rightmost(root):
    """
    Find the rightmost node of a tree.

    :param TreeNode root: root of the tree
    :returns (TreeNode): rightmost node of the tree
    """
    while root and root.right:
        root = root.right
    return root


def delete_iter(root, val):
    """
    Delete a node with a certain value, if it exists, from the
    tree having the given root.

    :param TreeNode root: root of the tree
    :param int val: value of the node to delete
    """
    while root:
        if val == root.val:

            # node to delete is leaf
            if not root.left and not root.right:
                if root == prev.right:
                    prev.right = None
                else:
                    prev.left = None
                return

            # node has right child
            if not root.left:
                if root == prev.right:
                    prev.right = root.right
                else:
                    prev.left = root.right
                return

            # node has left child
            if not root.right:
                if root == prev.right:
                    prev.right = root.left
                else:
                    prev.left = root.left
                return

            # node has left and right children
            rightmost = find_rightmost(root.left)
            rightmost.right = root.right
            if root == prev.right:
                prev.right = rightmost
            else:
                prev.left = rightmost
            return


        # iteratively traverse the tree
        elif val > root.val:
            prev = root
            root = root.right
        elif val < root.val:
            prev = root
            root = root.left


def test1():
    root = None
    rightmost = find_rightmost(root)
    assert rightmost == None
    print("test 1 successful")


def test2():
    root = TreeNode(2)
    rightmost = find_rightmost(root)
    assert rightmost == root
    print("test 2 successful")


def test3():
    right_right = TreeNode(7)
    right_left = TreeNode(5)
    right = TreeNode(6, right_left, right_right)
    left = TreeNode(2)
    root = TreeNode(4, left, right)
    rightmost = find_rightmost(root)
    assert rightmost == right_right
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
            TreeNode(5),
            TreeNode(7)
        )
    )
    lst = tree_to_list(root)
    assert lst == [1, 2, 3, 4, 5, 6, 7]
    print("test 4 successful")


def test5():
    root = TreeNode(
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
        )
    )
    delete_iter(root, 5)
    lst = tree_to_list(root)
    assert lst == [1, 2, 3, 4, 6, 7]
    print("test 5 successful")


def test6():
    root = TreeNode(
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
        )
    )
    delete_iter(root, 3)
    lst = tree_to_list(root)
    assert lst == [1, 2, 4, 5, 6, 7]
    print("test 6 successful")


def test7():
    root = TreeNode(
        4,
        TreeNode(
            2,
            TreeNode(1),
            TreeNode(3)
        ),
        TreeNode(
            7,
            TreeNode(6, TreeNode(5)),
        )
    )
    delete_iter(root, 7)
    lst = tree_to_list(root)
    assert lst == [1, 2, 3, 4, 5, 6]
    print("test 7 successful")


def test8():
    root = TreeNode(
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
        )
    )
    delete_iter(root, 2)
    lst = tree_to_list(root)
    assert lst == [1, 3, 4, 5, 6, 7]
    print("test 8 successful")


def test9():
    root = TreeNode(
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
        )
    )
    delete_iter(root, 6)
    lst = tree_to_list(root)
    assert lst == [1, 2, 3, 4, 5, 7]
    print("test 9 successful")


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()


if __name__ == "__main__":
    main()
