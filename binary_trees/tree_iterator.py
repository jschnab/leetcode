# leetcode challenge 173: binary tree iterator
# design a class to iterate over a binary tree
# this class implements the `next` method that returns
# the next smallest element of the tree, and the `has_next`
# method that determines if the next node exists


class BinaryTreeIterator:
    def __init__(self, root):
        """
        We initialize a stack of elements which is built by traversing
        the left subtree of the root, therefore placing the smallest
        element on top of the stack.
        """
        self.items = []  # stack of items
        self.traverse_left(root)

    def traverse_left(self, node):
        """
        The smallest element will always be the leftmost leaf node in the
        tree so we find it an build a stack while doing so. We can then
        pop the stack with `next` to return the current smallest element.

        Time complexity: O(n) in the worst case scenario (skewed tree)
        Space complexity: O(h) since we do a partial tree traversal
        """
        while node:
            self.items.append(node)
            node = node.left

    def next(self):
        """
        We pop the stack which maintains the smallest element on top by
        traversing the left of subtree under the right subtree of a node
        if it exists.

        Time complexity: O(1) we traverse the right side of the subtree
        under the current top node, which has a worst case time complexity
        of O(n), but in this case this is done once, the amortized complexity
        is then O(1)

        Space complexity: O(h)
        """
        top = self.items.pop()
        if top.right:
            self.traverse_left(top.right)
        return top.val

    def has_next(self):
        """
        The next element exists if the stack is not empty.

        Time complexity: O(1)
        """
        return self.items != []
