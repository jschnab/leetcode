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
    if node:
        postorder_recur(node.left, result)
        postorder_recur(node.right, result)
        result.append(node.val)


def preorder_iter(node):
    """
    Visit node, then explore left subtree, then explore right subtree (NLR).

    Iterative algorithm.

    :param Node node: Start node.
    :returns (list): Node values in prefix order.
    """
    result = []
    stack = [node]
    while stack:
        cur = stack.pop()
        result.append(cur.val)
        if cur.right is not None:
            stack.append(cur.right)
        if cur.left is not None:
            stack.append(cur.left)
    return result


def preorder_recur(node, result):
    """
    Visit node, then explore the left subtree, then explore the right subtree
    (NLR).

    Recursive algorithm.

    :param Node node: Start node.
    :param list result: List of node values, must be empty on initial call.
    """
    if node:
        result.append(node.val)
        preorder_recur(node.left, result)
        preorder_recur(node.right, result)


def inorder_recur(node, result):
    """
    Explore left subtree, then visit node, then explore right subtree (LNR).

    Recursive algorithm.

    :param Node node: Start node.
    :param list result: List of node values, must be empty on initial call.
    """
    if node:
        inorder_recur(node.left, result)
        result.append(node.val)
        inorder_recur(node.right, result)


def inorder_iter(node):
    """
    Explore left subtree, then visit node, then explore right subtree (LNR).

    Iterative algorithm.

    :param Node node: Start node.
    :returns (list): Node values sorted by infix order.
    """
    result = []
    stack = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.val)
            node = node.right
    return result


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


def test_preorder_recur():
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
    preorder_recur(root, result)
    assert result == [1, 2, 4, 5, 3, 6, 7]
    print("test preorder_recur successful")


def test_preorder_iter():
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
    result = preorder_iter(root)
    assert result == [1, 2, 4, 5, 3, 6, 7]
    print("test preorder_iter successful")


def test_inorder_recur():
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
    inorder_recur(root, result)
    assert result == [4, 2, 5, 1, 6, 3, 7]
    print("test inorder_recur successful")


def test_inorder_iter():
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
    result = inorder_iter(root)
    assert result == [4, 2, 5, 1, 6, 3, 7]
    print("test inorder_iter successful")


def main():
    test_postorder_iter()
    test_postorder_recur()
    test_preorder_recur()
    test_preorder_iter()
    test_inorder_recur()
    test_inorder_iter()


if __name__ == "__main__":
    main()
