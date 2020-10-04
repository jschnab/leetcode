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
    return TreeNode(node.val, copy_node(node.left), copy_node(node.right))


def merge(t1, t2):
    if not t1:
        return copy_node(t2)
    if not t2:
        return copy_node(t1)
    new = TreeNode(t1.val + t2.val)
    new.left = merge(t1.left, t2.left)
    new.right = merge(t1.right, t2.right)
    return new


def merge_iter(t1, t2):
    if not t1 and not t2:
        return
    t = TreeNode()
    stack = [(t, t1, t2)]
    while stack:
        n, n1, n2 = stack.pop()
        if n1 or n2:
            n.val = (n1.val if n1 else 0) + (n2.val if n2 else 0)
            if (n1 and n1.right) or (n2 and n2.right):
                n.right = TreeNode()
                stack.append((
                    n.right,
                    n1.right if n1 else None,
                    n2.right if n2 else None
                ))
            if (n1 and n1.left) or (n2 and n2.left):
                n.left = TreeNode()
                stack.append((
                    n.left,
                    n1.left if n1 else None,
                    n2.left if n2 else None
                ))
    return t


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
    assert lst == [4, 2, 5, 1, 6, 3, 7]
    print("test 1 successful")

def test2():
    t1 = TreeNode(
        val=1,
        left=TreeNode(3, TreeNode(5)),
        right=TreeNode(2)
    )
    t2 = TreeNode(
        val=2,
        left=TreeNode(1, None, TreeNode(4)),
        right=TreeNode(3, None, TreeNode(7))
    )
    t3 = merge(t1, t2)
    assert tree_to_list(t3, []) == [5, 4, 4, 3, 5, 7]
    print("test 2 successful")


def test3():
    t1 = TreeNode(
        val=1,
        left=TreeNode(3, TreeNode(5)),
        right=TreeNode(2)
    )
    t2 = TreeNode(
        val=2,
        left=TreeNode(1, None, TreeNode(4)),
        right=TreeNode(3, None, TreeNode(7))
    )
    t3 = merge_iter(t1, t2)
    assert tree_to_list(t3, []) == [5, 4, 4, 3, 5, 7]
    print("test 3 successful")



def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
