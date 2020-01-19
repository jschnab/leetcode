import collections

class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

        # answer for level order traversal
        self.result = []

        # answer for "smallest string from leaf"
        self.ans = '~'

        # answer for sum_between
        self.res = 0

        # for node inversion to match other tree
        self.flipped = []
        self.i = 0

        # result for paths summing up to target
        self.answer_pathsum = []

    def insert(self, data):
        """Insert a node in the tree.
        This function can be used to build a binary search tree
        from a preorder traversal node list."""

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def sum_between(self, root, L, R):
        """Return sum of node values if value between L and R."""
        self.res = 0
        self.L = L
        self.R = R
        def dfs(node):
            if node:
                dfs(node.left)
                if (node.data >= self.L) and (node.data <= self.R):
                    self.res += node.data
                dfs(node.right)
        dfs(root)
        return self.res

    def print_tree(self):
        """Print data stored in tree nodes."""
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def inorder_traversal(self, root):
        """Left -> root -> right"""
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(root.data)
            result = result + self.inorder_traversal(root.right)
        return result

    def preorder_traversal(self, root):
        """Root -> left -> right"""
        result = []
        if root:
            result.append(root.data)
            result = result + self.preorder_traversal(root.left)
            result = result + self.preorder_traversal(root.right)
        return result

    def postorder_traversal(self, root):
        """Left -> right -> root"""
        result = []
        if root:
            result = self.postorder_traversal(root.left)
            result = result + self.postorder_traversal(root.right)
            result.append(root.data)
        return result

    def height(self, node):
        """Return the height of the tree."""
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def get_level(self, root, level):
        """Get nodes from a given level."""
        if root is None:
            return
        if level == 1:
            self.result.append(root.data)
        elif level > 1:
            self.get_level(root.left, level-1)
            self.get_level(root.right, level-1)

    def level_order_traversal(self, root):
        self.result = []
        h = self.height(root)
        for i in range(1, h+1):
            self.get_level(root, i)
        return self.result

    def smallest_string_starting_from_leaf(self, root):
        """Print the smallest string starting from leaves.
A binary tree is filled numbers 0-25 representing code point for lowercase characters."""

        # perform a depth-first search
        def dfs(node, A):
            if node:

                # 'a' is 0
                A.append(chr(node.data + ord('a')))

                if not node.left and not node.right:

                    # the traversal goes from root to leaf so we reverse A
                    self.ans = min(self.ans, ''.join(reversed(A)))

                dfs(node.left, A)
                dfs(node.right, A)
                A.pop()

        dfs(root, [])
        print(self.ans)

    def vertical_traversal(self, root):
        """Traverse the tree vertically from left to right."""

        # we have a dictionary where keys are x coordinates,
        # values are dictionaries where keys are y coordinates,
        # values are list of nodes with x and y coordinates
        self.seen_nodes = collections.defaultdict(lambda: collections.defaultdict(list))

        def dfs(node, x=0, y=0):
            """Depth-first search and record node coordinates."""
            if node:
                self.seen_nodes[x][y].append(node)
                dfs(node.left, x - 1, y - 1)
                dfs(node.right, x + 1, y - 1)

        dfs(root)

        print(self.seen_nodes)
        answer = []
        for x in sorted(self.seen_nodes):
            record = []
            for y in sorted(self.seen_nodes[x]):
                record.extend(sorted(node.data for node in self.seen_nodes[x][y]))
            answer.append(record)

        return answer

    def flip_bin_tree_to_match(self, root, voyage):
        """Function which flips node of binary tree to match 'voyage'
which is a list of nodes corresponding to a tree."""

        def dfs(node):
            """Perform DFS and flip nodes on the fly if they don't match voyage."""
            if node:
                if node.data != voyage[self.i]:
                    self.flipped = [-1]
                    return

                self.i += 1

                if (self.i < len(voyage)) and node.left and node.left.data != voyage[self.i]:
                    self.flipped.append(node.data)
                    dfs(node.right)
                    dfs(node.left)

                else:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]
        return self.flipped

    def lowestCommonAncestor(self, root, p, q):
        """Print the lowest common ancestor of nodes p and q."""
        if root:
            if root.data < p.data and root.data < q.data:
                return self.lowestCommonAncestor(root.right, p, q)
            elif root.data > p.data and root.data > q.data:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                print(root.data)

    def pathSum(self, root, target):
        """Return the paths where node values sum up to target."""
        if not root:
            return []

        answer = []

        def dfs(node, path):
            if node:
                if not node.left and not node.right and sum(path) == target:
                    answer.append(path)

                if node.left:
                    dfs(node.left, path + [node.left.data])

                if node.right:
                    dfs(node.right, path + [node.right.data])

        dfs(root, [root.data])
        return answer

    def isBalanced(self, root):
        """Return True if the tree is balanced else False."""
        if not root:
            return True
        return abs(self.height(root.left) - self.height(root.right)) < 2 \
                and self.isBalanced(root.left) and self.isBalanced(root.right)

def sortedArrayToBST(array):
    """Transform sorted array into a binary search tree.
    [0,1,2,3,4,5] returns 2(0()(1))(4(3)(5))"""

    def recur(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = Node(array[mid])
        node.left = recur(left, mid - 1)
        node.right = recur(mid + 1, right)
        return node

    return recur(0, len(array) - 1)

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    #root.right.left = Node(0)
    root.right.right = Node(18)

    unbal = Node(1)
    unbal.left = Node(2)
    unbal.right = Node(2)
    unbal.left.left = Node(3)
    unbal.left.right = Node(3)
    unbal.left.left.left = Node(4)
    unbal.left.left.right = Node(4)

    bal = Node(10)
    bal.left = Node(20)
    bal.right = Node(30)
    bal.left.left = Node(40)
    bal.left.right = Node(50)
