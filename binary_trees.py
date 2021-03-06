from collections import deque


class TreeNode:
    """
    Node for a binary tree.
    """
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

    def print_tree(self):
        """
        Print the tree in a pre-order traversal.
        """
        if self:
            print(self.val)
            if self.left:
                self.left.print_tree()
            if self.right:
                self.right.print_tree()


def bst_from_array(array):
    """
    Make a binary search tree from a array of numbers.

    :param list array: list of numbers
    :return TreeNode: root of a binary search tree
    """
    def recurse(low, high):
        """
        Helper function which recursively build a binary search tree
        from a list of numbers using binary search.

        :param list array: list of numbers
        :param int low: index of the low boundary for binary search
        :param int high: index of the high boundary for binary search
        :return TreeNode:
        """
        if low > high:
            return None
        mid = (low + high) // 2
        node = TreeNode(array[mid])
        node.left = recurse(low, mid - 1)
        node.right = recurse(mid + 1, high)
        return node

    return recurse(0, len(array) - 1)


def dfs_pre_order(node):
    result = []
    q = []
    q.append(node)
    while q:
        current = q.pop()
        result.append(current.val)
        if current.right:
            q.append(current.right)
        if current.left:
            q.append(current.left)
    return result


def bfs(node):
    result = []
    q = deque()
    q.append(node)
    while q:
        current = q.popleft()
        result.append(current.val)
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
    return result


def sum_nodes_even_grandparents(root):
    """
    Leetcode biweekly contest 17, problem 1315
    Given a binary tree, return the sum of node values whose
    grandparents have even values. If there are no such nodes,
    return 0.

    :param TreeNode root: root of the binary tree
    :return int:
    """
    answer = 0
    q = []
    q.append(root)
    while q:
        current = q.pop()
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)

        if not current.val & 1:
            if current.left:
                if current.left.left:
                    answer += current.left.left.val
                if current.left.right:
                    answer += current.left.right.val
            if current.right:
                if current.right.left:
                    answer += current.right.left.val
                if current.right.right:
                    answer += current.right.right.val
    return answer


def remove_leaf_nodes(root, target):
    """
    Leetcode contest 172, problem 1325
    Given a binary tree, remove nodes which are leaves and if their value
    is a target value.

    This function uses recursion. We check each subtree and then check the
    root itself (base case).

    Time complexity: O(n)
    Space complexity: O(tree height) for call stack

    :param TreeNode root: root of the binary tree
    :return TreeNode: resulting tree
    """
    if root:
        root.left = remove_leaf_nodes(root.left, target)
        root.right = remove_leaf_nodes(root.right, target)
        if root.val == target and not root.left and not root.right:
            return
        return root


def remove_leaf_nodes_iter(root, target):
    """
    Leetcode contest 172, problem 1325
    Given a binary tree, remove nodes which are leaves and if their value
    is a target value.

    This function is iterative and uses depth-first search.
    To allow checking if the root itself should be removed in the end, I
    create a parent node for the root.
    Because new candidates for removal appear each time a leaf is removed,
    we need to traverse the tree one last time when no leaf needs to be
    removed. To allow this, we create a flag to determine when we should stop
    checking the tree for leaves to remove.

    Time complexity: O(n)
    Space complexity: O(n) for call stack

    :param TreeNode root: root of the binary tree
    :return TreeNode: resulting tree
    """

    # helper determines if node is leaf
    def is_leaf(node):
        if node.left is node.right:
            return True
        return False

    # helper determines if node is target
    def is_target(node, target):
        if node.val == target:
            return True
        return False

    head = TreeNode(0)
    head.left = root
    node_removed = True
    while node_removed:
        node_removed = False
        q = [head]
        while q:
            current = q.pop()
            if current.left:
                if is_leaf(current.left) and is_target(current.left):
                    current.left = None
                    node_removed = True
                else:
                    q.append(current.left)
            if current.right:
                if is_leaf(current.right) and is_target(current.right):
                    current.right = None
                    node_removed = True
                else:
                    q.append(current.right)
    return head.left


def same_tree_iter(p, q):
    """
    Checks if two binary trees are identical, iterative algorithm.

    Time complexity: O(N)
    Space complexity: O(logN) if balanced tree, O(N) worst case of completely
    unbalanced tree (keep a stack).

    :param TreeNode p: root of tree 1
    :param TreeNode q: root of tree 2
    :return bool: True if trees are identical else False
    """
    # helper function to check the identity of two nodes
    def check(p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return True

    # iterate throught the tree and check each pair of nodes
    # use DFS
    stack = []
    stack.append((p, q))
    while stack:
        p, q = stack.pop()
        if not check(p, q):
            return False
        # if check is True both p and q exist
        if p:
            stack.append((p.left, q.left))
            stack.append((p.right, q.right))

    return True


def same_tree_rec(p, q):
    """
    Checks if two binary trees are identical, recursive algorithm.

    Time complexity: O(N)
    Space complexity: O(logN) if balanced tree, O(N) worst case of a completely
    unbalanced tree (to keep recursion stack).

    :param TreeNode p: root of tree 1
    :param TreeNode q: root of tree 2
    :return bool: True if trees are identical else False
    """
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return same_tree_rec(p.left, q.left) and same_tree_rec(p.right, q.right)


def is_valid_tree_recur(n, left_children, right_children):
    """
    Leetcode problem 1361
    We have n binary tree nodes from 0 to n - 1 where node i has two children
    left_children[i] and right_children[i]. Return True if and only if all
    nodes form exactly one valid binary tree.

    :param int n: number of nodes
    :param list[int] left_children: left children of tree nodes
    :param list[int] right_children: right children of tree nodes
    :return bool: True if binary tree is valid
    """
    def dfs(i):
        if i in visited:
            return False
        if i == -1:
            return True
        visited.add(i)
        return dfs(left_children[i]) and dfs(right_children[i])

    visited = set()
    return dfs(0) and len(visited) == n


def is_valid_tree_iter(n, left_children, right_children):
    """
    Leetcode problem 1361
    See docstring of `is_valid_tree_recur()`.
    """
    # we use DFS with a list, but could use BFS with queue
    stack = [0]
    visited = set()
    while stack:
        current = stack.pop()
        if current in visited:
            return False
        visited.add(current)
        if left_children[current] != -1:
            stack.append(left_children[current])
        if right_children[current] != -1:
            stack.append(right_children[current])
    if len(visited) != n:
        return False
    return True


def list_in_tree(head, root):
    """
    Leetcode problem 1367
    Given a binary tree 'root' and a linked list 'head', return True if
    all nodes of the linked list correspond to some downward path (connected)
    in the tree. Otherwise, return False.

    We will have a helper function which finds the linked list in the tree,
    and the main function explores the tree and calls the helper function
    at every node of the tree.

    Time complexity: O(N * min(L, H)
    Space complexity: O(H)
    where N = tree size, H = tree height, L = list length
    """
    def helper(head, root):
        """
        Helper function which finds a connected downward path corresponding to
        the linked list in the tree.
        """
        # if we went through the whole list, we found the path
        if not head:
            return True

        # if we reach the end of a subtree without finding a correspondance
        # with the list
        if not root:
            return False

        # the current nodes from the list and tree match, as well as subsequent
        # nodes from the left or right subtree
        return head.val == root.val and (
            dfs(head.next, root.left) or dfs(head.next, root.right)
        )

    if not head:
        return True
    if not root:
        return False

    # call dfs to check if the list and tree correspond from the current node
    # otherwise check for correspondance from either left or right subtree
    return dfs(head, root) \
        or list_in_tree(head, root.left) \
        or list_in_tree(head, root.right)


if __name__ == "__main__":
    pass
