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


def delete_recur(root, val):
    """
    Delete a node with a certain value, if it exists, from the
    tree having the given root.

    :param TreeNode root: root of the tree
    :param int val: value of the node to delete
    """
    if not root:
        return

    if root.val == val and not root.left and not root.right:
        return

    if root.val == val and root.left and not root.right:
        return root.left

    if root.val == val and not root.left and root.right:
        return root.right

    if root.val == val and root.left and root.right:
        rightmost = find_rightmost(root.left)
        root.val = rightmost.val
        root.left = delete_recur(root.left, rightmost.val)
        return root

    if val < root.val:
        root.left = delete_recur(root.left, val)
    elif val > root.val:
        root.right = delete_recur(root.right, val)

    return root


def delete_iter(root, val):
    """
    Delete a node with a certain value, if it exists, from the
    tree having the given root.

    :param TreeNode root: root of the tree
    :param int val: value of the node to delete
    """
    dummy = TreeNode(right=root)
    prev = dummy
    node = root
    while node:
        if val == node.val:

            # node to delete is leaf
            if not node.left and not node.right:
                if node == prev.right:
                    prev.right = None
                else:
                    prev.left = None
                return dummy.right

            # node has right child
            if not node.left:
                if node == prev.right:
                    prev.right = node.right
                else:
                    prev.left = node.right
                return dummy.right

            # node has left child
            if not node.right:
                if node == prev.right:
                    prev.right = node.left
                else:
                    prev.left = node.left
                return dummy.right

            # node has left and right children
            rightmost = find_rightmost(node.left)
            rightmost.left = delete_iter(node.left, rightmost.val)
            rightmost.right = node.right
            if node == prev.right:
                prev.right = rightmost
            else:
                prev.left = rightmost
            return dummy.right


        # iteratively traverse the tree
        elif val > node.val:
            prev = node
            node = node.right
        elif val < node.val:
            prev = node
            node = node.left

    return dummy.right


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
    root = delete_iter(root, 5)
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
    root = delete_iter(root, 3)
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
    root = delete_iter(root, 7)
    lst = tree_to_list(root)
    assert lst == [1, 2, 3, 4, 5, 6]
    print("test 7 successful")


def test7bis():
    root = TreeNode(2)
    root = delete_iter(root, 2)
    assert root is None
    print("test 7bis successful")


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
    root = delete_iter(root, 2)
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
    root = delete_iter(root, 6)
    lst = tree_to_list(root)
    assert lst == [1, 2, 3, 4, 5, 7]
    print("test 9 successful")


def test10():
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
    root = delete_iter(root, 4)
    lst = tree_to_list(root)
    assert lst == [1, 2, 3, 5, 6, 7]
    print("test 10 successful")


def test11():
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
    root = delete_iter(root, -1)
    lst = tree_to_list(root)
    assert lst == [1, 2, 3, 4, 5, 6, 7]
    print("test 11 successful")


def test12():
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
    root = delete_recur(root, 1)
    lst = tree_to_list(root)
    assert lst == [2, 3, 4, 5, 6, 7]
    print("test 12 successful")


def test13():
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
    root = delete_recur(root, 7)
    lst = tree_to_list(root)
    assert lst == [1, 2, 3, 4, 5, 6]
    print("test 13 successful")


def test14():
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
    root = delete_recur(root, 4)
    lst = tree_to_list(root)
    assert lst == [1, 2, 3, 5, 6, 7]
    print("test 14 successful")


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test7bis()
    test8()
    test9()
    test10()
    test11()
    test12()
    test13()
    test14()


if __name__ == "__main__":
    main()
