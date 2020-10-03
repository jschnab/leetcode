# leetcode challenge 617: merge two binary trees

# given two binary trees and imagine that when you put one to cover the other
# some nodes of the two trees are overlapped while others are not
# you need to merge two trees into a new binary tree, the merge rule is that
# if two nodes overlap, then we sum node values up as the new value of the
# merged node
# otherwise, the not-null node is used as the node of the new tree

# input: [1, 3, 2, 5], [2, 1, 3, null, 4, null, 7]
# output: [3, 4, 5, 5, 4, null, 7]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def copy_node(node):
    if not node:
        return
    return TreeNode(node.val, node.left, node.right)


def merge(t1, t2):
    if not t1:
        return copy_node(t2)
    if not t2:
        return copy_node(t1)
    new = TreeNode(t1.val + t2.val)
    new.left = merge(t1.left, t2.left)
    new.right = merge(t1.right, t2.right)
    return new


def tree_to_list(root, lst=None):
    if root is None:
        return
    tree_to_list(root.left, lst)
    lst.append(root.val)
    tree_to_list(root.right, lst)
    return lst


def test1():
    root = TreeNode(
        val=1,
        left=TreeNode(2, TreeNode(4), TreeNode(5)),
        right=TreeNode(3, TreeNode(6), TreeNode(7))
    )
    lst = tree_to_list(root, [])
    print(lst)


def test2():
    t1 = TreeNode(
        val=1,
        left=TreeNode(3, TreeNode(5)),
        right=TreeNode(2)
    )
    print("t1:", tree_to_list(t1, []))
    t2 = TreeNode(
        val=2,
        left=TreeNode(1, None, TreeNode(4)),
        right=TreeNode(3, None, TreeNode(7))
    )
    print("t2:", tree_to_list(t2, []))
    t3 = merge(t1, t2)
    print("t3:", tree_to_list(t3, []))


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
