from collections import deque


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height(root):
    if root:
        return 1 + max(height(root.left), height(root.right))
    return 0


def is_balanced(root):
    q = deque([root])
    while len(q) > 0:
        node = q.pop()
        if node:
            if abs(height(root.left) - height(root.right)) > 1:
                return False
            q.appendleft(node.left)
            q.appendleft(node.right)
    return True


def check_height(root):
    """
    Returns -1 if tree is unbalanced, else height difference between
    left and right subtrees.
    """
    if not root:
        return 0

    left_height = check_height(root.left)
    if left_height == -1:
        return -1

    right_height = check_height(root.right)
    if right_height == -1:
        return -1

    diff = abs(left_height - right_height)
    if diff > 1:
        return -1

    return max(left_height, right_height) + 1


def is_balanced2(root):
    if check_height(root) == -1:
        return False
    return True


def test1():
    root = TreeNode(1)
    assert height(root) == 1
    print("test 1 successful")


def test2():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert height(root) == 2
    print("test 2 successful")


def test3():
    root = TreeNode(
        1,
        TreeNode(2),
        TreeNode(
            3,
            TreeNode(4),
            TreeNode(5)
        )
    )
    assert height(root) == 3
    print("test 3 successful")


def test4():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_balanced(root) == True
    print("test 4 successful")


def test5():
    root = TreeNode(
        1,
        TreeNode(2),
        TreeNode(
            3,
            TreeNode(4),
            TreeNode(5)
        )
    )
    assert is_balanced(root) == True
    print("test 5 successful")


def test6():
    root = TreeNode(
        1,
        TreeNode(2),
        TreeNode(
            3,
            TreeNode(4),
            TreeNode(5, TreeNode(6))
        )
    )
    assert is_balanced(root) == False
    print("test 6 successful")


def test7():
    root = TreeNode(1)
    assert check_height(root) == 1
    print("test 7 successful")


def test8():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert check_height(root) == 2
    print("test 8 successful")


def test9():
    root = TreeNode(
        1,
        TreeNode(2),
        TreeNode(
            3,
            TreeNode(4),
            TreeNode(5)
        )
    )
    assert check_height(root) == 3
    print("test 9 successful")


def test10():
    root = TreeNode(
        1,
        TreeNode(2),
        TreeNode(
            3,
            TreeNode(4),
            TreeNode(5, TreeNode(6))
        )
    )
    assert check_height(root) == -1
    print("test 10 successful")


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
    test10()


if __name__ == "__main__":
    main()
