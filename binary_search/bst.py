from collections import deque


class Node:
    def __init__(self, val=None, par=None, left=None, right=None):
        self.val = val
        self.par = par
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node({self.val})"

    def __repr__(self):
        return str(self)


class Tree:
    def __init__(self, root=None):
        self.root = root

    def add(self, val):
        x = self.root
        y = None
        while x is not None:
            y = x
            if val < x.val:
                x = x.left
            else:
                x = x.right
        new = Node(val, y)
        if y is None:
            self.root = new
        elif val < y.val:
            y.left = new
        else:
            y.right = new

    def values(self, root=None):
        node = root or self.root
        stack = []
        result = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right
        return result

    def find(self, val):
        node = self.root
        while node is not None:
            if node.val == val:
                return node
            if val < node.val:
                node = node.left
            else:
                node = node.right

    def mini(self, root=None):
        node = root or self.root
        while node.left is not None:
            node = node.left
        return node

    def _transplant(self, x, y):
        if x.par is None:
            self.root = y
        elif x is x.par.left:
            x.par.left = y
        else:
            x.par.right = y
        if y is not None:
            y.par = x.par

    def delete(self, node):
        if node.left is None:
            self._transplant(node, node.right)
        elif node.right is None:
            self._transplant(node, node.left)
        else:
            mini = self.mini(node.right)
            if node is not mini.par:
                self._transplant(mini, mini.right)
                mini.right = node.right
                mini.right.par = mini
            self._transplant(node, mini)
            mini.left = node.left
            mini.left.par = mini

    def height(self, root=None):
        """
        Height of node is number of edges in longest path from node to leaf.
        Height of tree is height of root.
        """
        node = root or self.root
        stack = [(node, 0)]
        height = 0
        while stack != []:
            node, depth = stack.pop()
            height = max(height, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return height

    def diameter(self, root=None):
        def helper(node):
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            nonlocal d
            d = max(d, left + right)
            return 1 + max(left, right)

        d = 0
        node = root or self.root
        helper(node)
        return d

    def width(self, root=None):
        """
        Maximum number of nodes across all depths of the tree.
        """
        root = root or self.root
        if root is None:
            return 0
        max_width = 0
        q = deque([root])
        while len(q) > 0:
            width = len(q)
            max_width = max(max_width, width)
            for _ in range(width):
                node = q.pop()
                if node.left is not None:
                    q.appendleft(node.left)
                if node.right is not None:
                    q.appendleft(node.right)
        return max_width

    def successor(self, node):
        """
        If  node has no right child but has a successor, successor is lowest
        ancestor of node whose left child is also an ancestor of node.
        """
        if node.right:
            return self.mini(node.right)
        p = node.par
        while p is not None and p.right is node:
            node = p
            p = p.par
        return p


def make_tree():
    t = Tree()
    t.add(4)
    t.add(2)
    t.add(6)
    t.add(1)
    t.add(3)
    t.add(5)
    t.add(7)
    return t


def test_add():
    t = make_tree()
    assert t.values() == [1, 2, 3, 4, 5, 6, 7]
    print("test add successful")


def test_find():
    t = make_tree()
    assert t.find(4) == t.root
    assert t.find(2) == t.root.left
    assert t.find(6) == t.root.right
    print("test find successful")


def test_delete():
    t = make_tree()
    t.delete(t.find(1))
    assert t.values() == [2, 3, 4, 5, 6, 7]
    t.delete(t.find(2))
    assert t.values() == [3, 4, 5, 6, 7]
    t.delete(t.find(7))
    t.delete(t.find(6))
    assert t.values() == [3, 4, 5]
    t.delete(t.find(4))
    assert t.values() == [3, 5]
    print("test delete successful")


def test_height():
    t = make_tree()
    assert t.height() == 2
    t.add(0)
    assert t.height() == 3
    t.add(8)
    assert t.height() == 3
    print("test height successful")


def test_diameter():
    t = make_tree()
    assert t.diameter() == 4
    t.add(0)
    t.add(-1)
    t.add(-2)
    t.add(3.5)
    t.add(3.6)
    t.add(3.7)
    assert t.diameter() == 8
    print("test diameter successful")


def test_successor():
    t = make_tree()
    assert t.successor(t.find(4)) == t.find(5)
    assert t.successor(t.find(2)) == t.find(3)
    assert t.successor(t.find(3)) == t.find(4)
    assert t.successor(t.find(5)) == t.find(6)
    print("test successor successful")


def test_width():
    t = Tree()
    assert t.width() == 0
    t.add(4)
    assert t.width() == 1
    t.add(2)
    assert t.width() == 1
    t.add(6)
    assert t.width() == 2
    t.add(1)
    assert t.width() == 2
    t.add(5)
    assert t.width() == 2
    t.add(3)
    assert t.width() == 3
    t.add(7)
    assert t.width() == 4
    print("test width successful")


def main():
    test_add()
    test_find()
    test_delete()
    test_height()
    test_diameter()
    test_successor()
    test_width()


if __name__ == "__main__":
    main()
