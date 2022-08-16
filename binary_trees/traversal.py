class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder_iter(node):
    """
    Explore the left subtree, then the right subtree, then visit node (LRN).

    Iterative algorithm.

    :param Node node: Start node.
    :returns (list): Node values in post-order.
    """
    result = []
    stack = []
    last = None
    while stack or node:
        if node:
            # put the node aside and keep exploring the left subtree
            stack.append(node)
            node = node.left
        else:
            # here, we either finished exploring the left or right subtree
            peek = stack[-1]
            if peek.right and last != peek.right:
                # if not yet explored right subtree, explore it
                node = peek.right
            else:
                # if already explored right subtree, visit node
                result.append(peek.val)
                last = stack.pop()
    return result


def postorder_recur(node, result):
    """
    Explore the left subtree, then the right subtree, then visit node (LRN).

    Recursive algorithm.

    :param Node node: Start node.
    :param list result: List of node values, must be empty on initial call.
    """
    if node.left:
        postorder_recur(node.left, result)
    if node.right:
        postorder_recur(node.right, result)
    result.append(node.val)


def test_postorder_iter():
    root = Node(
        1,
        Node(
            2,
            Node(4),
            Node(5)
        ),
        Node(
            3,
            Node(6),
            Node(7)
        )
    )
    assert postorder_iter(root) == [4, 5, 2, 6, 7, 3, 1]
    print("test postorder iter successful")


def test_postorder_recur():
    root = Node(
        1,
        Node(
            2,
            Node(4),
            Node(5)
        ),
        Node(
            3,
            Node(6),
            Node(7)
        )
    )
    result = []
    postorder_recur(root, result)
    assert result == [4, 5, 2, 6, 7, 3, 1]
    print("test postorder_recur successful")


def main():
    test_postorder_iter()
    test_postorder_recur()


if __name__ == "__main__":
    main()
