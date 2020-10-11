# leetcode challenge 589: N-ary tree preorder traversal

# input:  [1,3,2,4,5,6]
# output: [1,3,5,6,2.4]


class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []


def preorder_iter(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        for i in range(len(node.children)-1, -1, -1):
            stack.append(node.children[i])
    return result


def preorder_recur(root):
    def helper(root):
        nonlocal result
        if not root:
            return
        result.append(root.val)
        for child in root.children:
            helper(child)

    result = []
    helper(root)
    return result


def preorder_recur2(root, result):
    if root:
        result.append(root.val)
        for child in root.children:
            preorder_recur2(child, result)
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
    expected = [1, 3, 5, 6, 2, 4]
    assert preorder_iter(t) == expected
    assert preorder_recur(t) == expected
    assert preorder_recur2(t, []) == expected
    print("test 1 successful")


def test2():
    t = None
    expected = []
    assert preorder_iter(t) == expected
    assert preorder_recur(t) == expected
    assert preorder_recur2(t, []) == expected
    print("test 2 successful")


def test3():
    t = TreeNode(5)
    expected = [5]
    assert preorder_iter(t) == expected
    assert preorder_recur(t) == expected
    assert preorder_recur2(t, []) == expected
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
