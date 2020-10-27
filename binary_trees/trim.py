# leetcode challenge 669: trim a binary search tree
# given the root of a BST and a low and a high boundary, trim the tree
# so that all elements lie in the inclusive interval [low, high]
# return the root of the trimmed BST

# input:  [1, 0, 2], low = 1, high = 2
# output: [1, 2]

# input:  [3, 0, 4, 2, 1], low = 1, high = 3
# output: [3, 2, 1]


def helper(root, low, high):
    """
    Time complexity: O(n) we visit each node in the tree
    Space complexity: O(n) the recursion call stack has up to n depth
    """
    if not root:
        return
    if root.val < low:

        return trim(root.right, low, high)
    if root.val > high:
        return trim(root.left, low, high)

    root.left = trim(root.left, low, high)
    root.right = trim(root.right, low, high)

    return root


def trim(root, low, high):
    return helper(root, low, high)


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def to_list(root, lst):
    if root:
        to_list(root.left, lst)
        lst.append(root.val)
        to_list(root.right, lst)
    return lst


def test1():
    t = TreeNode(
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
    lst = to_list(t, [])
    assert lst == [1, 2, 3, 4, 5, 6, 7]
    print("test 1 successful")


def test2():
    t = TreeNode(1, TreeNode(0), TreeNode(2))
    assert to_list(trim(t, 1, 2), []) == [1, 2]
    print("test 2 successful")


def test3():
    t = TreeNode(
        3,
        TreeNode(0, None, TreeNode(2, TreeNode(1))),
        TreeNode(4)
    )
    assert to_list(trim(t, 1, 3), []) == [1, 2, 3]
    print("test 3 successful")


def test4():
    t = TreeNode(1)
    assert to_list(trim(t, 1, 2), []) == [1]
    print("test 4 successful")


def test5():
    t = TreeNode(1, None, TreeNode(2))
    assert to_list(trim(t, 1, 3), []) == [1, 2]
    print("test 5 successful")


def test6():
    t = TreeNode(1, None, TreeNode(2))
    assert to_list(trim(t, 2, 4), []) == [2]
    print("test 6 successful")


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()


if __name__ == "__main__":
    main()
