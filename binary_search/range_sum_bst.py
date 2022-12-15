"""
leetcode 938: range sum of BST

Given the root node of a binary search tree and two integers low and high,
return the sumb of the values of all nodes with a value in the inclusive range
[low, high].
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def range_sum(root, low, high):
    if not root:
        return 0
    val = 0
    if root.val >= low and root.val <= high:
        val = root.val
    return val + range_sum(root.left, low, high) + range_sum(
        root.right, low, high
    )


def test1():
    root = Node(10, Node(5, Node(3), Node(7)), Node(15, None, Node(18)))
    assert range_sum(root, 7, 15) == 32
    print("test 1 successful")


def test2():
    root = Node(
        10,
        Node(
            5,
            Node(3, Node(1)),
            Node(7, Node(6))
        ),
        Node(15, Node(13), Node(18))
    )
    assert range_sum(root, 6, 10) == 23
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
