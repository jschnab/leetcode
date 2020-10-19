from collections import deque

# leetcode challenge 559: maximum depth of n-ary tree
# given an n-ary tree, find it's maximum depth, i.e. the number of nodes
# along the longest path from the root node down to the farthest leaf node

class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []


def max_depth(root):
    if not root:
        return 0
    if root.children:
        return 1 + max(max_depth(child) for child in root.children)
    return 1


def max_depth_iter(root):
    if not root:
        return 0

    q = deque([root])
    result = 0
    while q:
        count = len(q)
        result += 1
        for _ in range(count):
            node = q.pop()
            for child in node.children:
                q.appendleft(child)

    return result


def test1():
    root = None
    depth = max_depth(root)
    assert depth == 0
    print("test 1 successful")


def test2():
    root = TreeNode(3)
    depth = max_depth(root)
    assert depth == 1
    print("test 2 successful")


def test3():
    root = TreeNode(
        3,
        [
            TreeNode(2), TreeNode(7),
        ]
    )
    depth = max_depth(root)
    assert depth == 2
    print("test 3 successful")


def test4():
    root = None
    depth = max_depth_iter(root)
    assert depth == 0
    print("test 1 successful")


def test5():
    root = TreeNode(3)
    depth = max_depth_iter(root)
    assert depth == 1
    print("test 5 successful")


def test6():
    root = TreeNode(
        3,
        [
            TreeNode(2), TreeNode(7),
        ]
    )
    depth = max_depth(root)
    assert depth == 2
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
