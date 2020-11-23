

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def contains(root, val):
    if root:
        if root.val == val:
            return True
        return contains(root.left, val) or contains(root.right, val)
    return False


def helper(t1, t2):
    if t1 and t2:
        if t1.val != t2.val:
            return False
        return helper(t1.left, t2.left) and helper(t1.right, t2.right)
    return True


def is_subtree(t1, t2):
    if not t1:
        return False
    if not t2:
        return True
    stack = [t1]
    root = None
    while stack:
        node = stack.pop()
        if node.val == t2.val:
            root = node
            break
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    if root:
        return helper(root, t2)
    return False


def test1():
    root = TreeNode(
        "A",
        TreeNode(
            "B",
            TreeNode("D"),
            TreeNode("E")
        ),
        TreeNode(
            "C",
            TreeNode("F"),
            TreeNode("G")
        )
    )
    assert contains(root, "G") is True
    print("test 1 successful")


def test2():
    root = TreeNode(
        "A",
        TreeNode(
            "B",
            TreeNode("D"),
            TreeNode("E")
        ),
        TreeNode(
            "C",
            TreeNode("F"),
            TreeNode("G")
        )
    )
    assert contains(root, "Z") is False
    print("test 2 successful")


def test3():
    t1 = TreeNode(
        "A",
        TreeNode(
            "B",
            TreeNode("D"),
            TreeNode("E")
        ),
        TreeNode(
            "C",
            TreeNode("F"),
            TreeNode("G")
        )
    )
    t2 = TreeNode("C", TreeNode("F"), TreeNode("G"))
    assert helper(t1.right, t2) is True
    print("test 3 successful")


def test4():
    t1 = TreeNode(
        "A",
        TreeNode(
            "B",
            TreeNode("D"),
            TreeNode("E")
        ),
        TreeNode(
            "C",
            TreeNode("F"),
            TreeNode("G")
        )
    )
    t2 = TreeNode("C", TreeNode("F"), TreeNode("G"))
    assert helper(t1, t2) is False
    print("test 4 successful")


def test5():
    t1 = TreeNode(
        "A",
        TreeNode(
            "B",
            TreeNode("D"),
            TreeNode("E")
        ),
        TreeNode(
            "C",
            TreeNode("F"),
            TreeNode("G")
        )
    )
    t2 = TreeNode("C", TreeNode("F"), TreeNode("G"))
    assert is_subtree(t1, t2) is True
    print("test 5 successful")


def test6():
    t1 = None
    t2 = TreeNode("C", TreeNode("F"), TreeNode("G"))
    assert is_subtree(t1, t2) is False
    print("test 6 successful")


def test7():
    t1 = TreeNode(
        "A",
        TreeNode(
            "B",
            TreeNode("D"),
            TreeNode("E")
        ),
        TreeNode(
            "C",
            TreeNode("F"),
            TreeNode("G")
        )
    )
    t2 = None
    assert is_subtree(t1, t2) is True
    print("test 7 successful")


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()


if __name__ == "__main__":
    main()
