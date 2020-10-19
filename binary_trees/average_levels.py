from collections import deque

# leetcode challenge 637: average of levels in binary tree
# given a non-empty binary tree, return the average value of the nodes
# on each level in the form of an array

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def average_levels(root):
    if not root:
        return []

    result = []
    q = deque([root])
    while q:
        count = len(q)
        sum_ = 0
        for _ in range(count):
            node = q.pop()
            sum_ += node.val
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)
        result.append(sum_ / count)
    return result


def test1():
    root = None
    avg = average_levels(root)
    assert avg == []
    print("test 1 successful")


def test2():
    root = TreeNode(2)
    avg = average_levels(root)
    assert avg == [2]
    print("test 2 successful")


def test3():
    root = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3)
    )
    avg = average_levels(root)
    assert avg == [1, 2.5]
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
