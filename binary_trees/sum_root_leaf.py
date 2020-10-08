# leetcode challenge 1022: sum of root-to-leaf binary numbers
# we are given the root of a binary tree where each node has as value 0 or 1
# each root-to-leaf path represents a binary number starting with the most
# significant bit, e.g. 0 -> 1 -> 1 -> 0 represents 0110, which is 6
# for all leaves in the tree, return the sum of the numbers which represent
# the path from the root to that leaf

# input:  [1, 0, 1, 0, 1, 0, 1]
# output: 22

# input:  [0]
# output: 0

# input:  [1, 1]
# output: 3


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def root_leaf_recur(root):
    def helper(root, sum_):
        nonlocal result
        sum_ = (sum_ << 1) + root.val
        if not root.left and not root.right:
            result += sum_
        if root.left:
            helper(root.left, sum_)
        if root.right:
            helper(root.right, sum_)

    result = 0
    helper(root, 0)
    return result


def root_leaf_iter(root):
    result = 0
    stack = [(root, 0)]
    while stack:
        node, sum_ = stack.pop()
        sum_ = (sum_ << 1) + node.val
        if not node.left and not node.right:
            result += sum_
        if node.right:
            stack.append((node.right, sum_))
        if node.left:
            stack.append((node.left, sum_))
    return result


def test1():
    t = TreeNode(1, TreeNode(0), TreeNode(1))
    assert root_leaf_recur(t) == 5
    assert root_leaf_iter(t) == 5
    print("test 1 successful")


def test2():
    t = TreeNode(
        1,
        TreeNode(
            0,
            TreeNode(0),
            TreeNode(1)
        ),
        TreeNode(
            1,
            TreeNode(0),
            TreeNode(1)
        )
    )
    assert root_leaf_recur(t) == 22
    assert root_leaf_iter(t) == 22
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
