"""
leetcode 2331: evaluate boolean binary tree

We are given the root of a full binary tree with the following properties:
- leaf nodes have either the value 0 or 1, representing False or True
- non-leaf nodes have either the value 2 or 3, where 2 represents boolean OR
  and 3 represents the boolean AND

To evaluate a node:
- leaf node evaluates as the value of the node
- other nodes evaluate as the boolean operation of the value of their subtrees

Return the boolean result of evaluating the root node.

Notes: A full binary tree is a binary tree where each node has either 0 or 2
children.
"""


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def evaluate(root):
    """
    We traverse the tree to collect operators and operands using depth-first
    search postorder, which puts them in reverse Polish notation. This will
    allow us to evaluate the operands with a simple stack.
    """
    tokens = []
    stack = []
    last = None
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            peek = stack[-1]
            if peek.right and peek.right != last:
                root = peek.right
            else:
                tokens.append(peek.val)
                last = stack.pop()
    for t in tokens:
        if t in [0, 1]:
            stack.append(t)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if t == 2:
                stack.append(op1 or op2)
            elif t == 3:
                stack.append(op1 and op2)
    return bool(stack[-1])


def test1():
    root = Node(
        2,
        Node(1),
        Node(
            3,
            Node(0),
            Node(1)
        ),
    )
    assert evaluate(root) is True
    print("test 1 successful")


def test2():
    root = Node(0)
    assert evaluate(root) is False
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
