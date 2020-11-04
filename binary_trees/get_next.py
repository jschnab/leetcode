# given a binary search tree node, get the value of the next node


class TreeNode:
    def __init__(self, val=None, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


# the function get_next() is better than this one
def get_next2(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node

    # this is covered by the next block
    if node == node.parent.left:
        return node.parent

    # cleaner code if we store both node and parent
    if node == node.parent.right:
        while node.parent and node.parent.left != node:
            node = node.parent
        if node.parent and node == node.parent.left:
            return node.parent


def get_next(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node

    parent = node.parent
    while parent and parent.left != node:
        node = parent
        parent = parent.parent
    return parent


def test():
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)

    one.parent = two
    two.left = one
    two.right = three
    two.parent = four
    three.parent = two
    four.left = two
    four.right = six
    six.parent = four
    six.left = five
    six.right = seven
    five.parent = six
    seven.parent = six

    assert get_next(one) == two
    assert get_next(two) == three
    assert get_next(three) == four
    assert get_next(four) == five
    assert get_next(five) == six
    assert get_next(six) == seven
    assert get_next(seven) is None
    print("test successful")


def main():
    test()


if __name__ == "__main__":
    main()
