# leetcode challenge 590: N-ary tree postorder traversal

class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []


def postorder_iter(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        for child in node.children:
            stack.append(child)
    return result[::-1]


def postorder_recur(root, result):
    if root:
        for child in root.children:
            postorder_recur(child, result)
        result.append(root.val)
        return result
    return []


def test1():
    t = TreeNode(
        1,
        [
            TreeNode(3, [TreeNode(5), TreeNode(6)]),
            TreeNode(2),
            TreeNode(4),
        ]
    )
    expected = [5, 6, 3, 2, 4, 1]
    assert postorder_iter(t) == expected
    assert postorder_recur(t, []) == expected
    print("test 1 successful")


def test2():
    t = None
    expected = []
    assert postorder_iter(t) == expected
    assert postorder_recur(t, []) == expected
    print("test 2 successful")


def test3():
    t = TreeNode(5)
    expected = [5]
    assert postorder_iter(t) == expected
    assert postorder_recur(t, []) == expected
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
