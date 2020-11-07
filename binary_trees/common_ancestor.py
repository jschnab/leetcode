# get the first common ancestor of two nodes of a binary tree


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def helper(node, target, parents, result):
    if node:
        copy = parents.copy()
        copy.append(node)
        helper(node.left, target, copy, result)
        helper(node.right, target, copy, result)
        if node.val == target:
            result.append(copy)


def get_parents(root, node_value):
    """
    Get the list of parents of a node.

    :param TreeNode root: root of the tree
    :param node_val: value of the node to get the parents of
    :returns (list): list of parents nodes
    """
    result = []
    helper(root, node_value, [], result)
    return [n for n in result[0] if node_value != n.val]


def get_children(root):
    """
    Get the set of node values children from root.

    :param TreeNode root: root of the tree
    :returns (set): set of node values
    """
    if not root:
        return set()
    result = set()
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            result.add(node.val)
            stack.append(node.left)
            stack.append(node.right)
    return result - {root.val}


def get_common_ancestor(tree, a, b):
    """
    Get the first common ancestor of two TreeNode instances a and b.

    :param TreeNode root: root of the tree
    :param TreeNode a: first node
    :param TreeNode b: second node
    :returns (TreeNode): first common ancestor of a and b
    """
    # reverse list of parents to have root at the end
    parents = get_parents(tree, a.val)[::-1]
    for p in parents:
        children = get_children(p)
        if a.val in children and b.val in children:
            return p


def get_node_values(root):
    """
    Return a set of node values by traversing the tree
    using depth-first search in a preorder fashion.

    :param TreeNode root: root of the tree
    :returns (set): set of node values
    """
    if not root:
        return set()
    result = set()
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            result.add(node.val)
            stack.append(node.left)
            stack.append(node.right)
    return result


def get_common_ancestor2(root, a, b):
    """
    Get the first common ancestor of two nodes a and b.
    Assumes nodes values are unique.

    Time complexity: O(n), if the tree is balanced we first traverse n/2
        nodes (left subtree), then n/4, etc
    Space complexity: O(logn), the size of the recursion stack is the height
        of the tree

    :param TreeNode root: root of the tree
    :param TreeNode a: first node
    :param TreeNode b: second node
    :returns (TreeNode): first common ancestor of a and b
    """
    if (not root) or (a is root) or (b is root):
        return

    left_children = get_node_values(root.left)

    # if a and b are in different subtrees we have the common ancestor
    if (a.val in left_children) ^ (b.val in left_children):
        return root

    # if a and b are in the left subtree, recurse throught this tree
    if a.val in left_children:
        return get_common_ancestor2(root.left, a, b)

    # a and b are in the right subtree
    return get_common_ancestor2(root.right, a, b)


def test1():
    tree = TreeNode(
        "A",
        TreeNode(
            "B",
            TreeNode("D"),
            TreeNode("E")
        ),
        TreeNode(
            "C",
            TreeNode("F"),
            TreeNode("G")
        )
    )
    result = get_parents(tree, "G")
    assert [node.val for node in result] == ["A", "C"]
    print("test 1 successful")


def test2():
    tree = TreeNode(
        "A",
        TreeNode(
            "B",
            TreeNode("D"),
            TreeNode("E")
        ),
        TreeNode(
            "C",
            TreeNode("F"),
            TreeNode("G")
        )
    )
    children = get_children(tree.left)
    assert children == set(["D", "E"])
    print("test 2 successful")


def test3():
    tree = TreeNode(
        "A",
        TreeNode(
            "B",
            TreeNode("D"),
            TreeNode("E")
        ),
        TreeNode(
            "C",
            TreeNode("F"),
            TreeNode("G")
        )
    )
    B = tree.left
    D = tree.left.left
    E = tree.left.right
    assert get_common_ancestor(tree, D, E) == B
    assert get_common_ancestor2(tree, D, E) == B
    print("test 3 successful")


def test4():
    tree = TreeNode(
        "A",
        TreeNode(
            "B",
            TreeNode("D"),
            TreeNode("E")
        ),
        TreeNode(
            "C",
            TreeNode("F"),
            TreeNode("G")
        )
    )
    D = tree.left.left
    F = tree.right.left
    assert get_common_ancestor(tree, D, F) == tree
    assert get_common_ancestor2(tree, D, F) == tree
    print("test 4 successful")


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
