import random
import statistics
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"Node({self.val})"

    def __str__(self):
        return repr(self)


class Tree:
    def __init__(self, root_val=None):
        self.root = None
        self.median_node = None
        self.size = 0
        if root_val is not None:
            self.root = Node(root_val)
            self.median_node = self.root
            self.size = 1

    def __repr__(self):
        return repr(self.inorder())

    def __str__(self):
        return str(self.inorder())

    def inorder(self):
        result = []
        node = self.root
        stack = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right
        return result

    def preorder(self):
        if self.root is None:
            return []
        result = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return result

    def postorder(self):
        result = []
        stack = []
        node = self.root
        last = None
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek = stack[-1]
                if peek.right and last is not peek.right:
                    node = peek.right
                else:
                    last = stack.pop()
                    result.append(last.val)
        return result

    def mini(self, node):
        while node.left is not None:
            node = node.left
        return node

    def maxi(self, node):
        while node.right is not None:
            node = node.right
        return node

    def successor(self, node):
        if node.right is not None:
            return self.mini(node.right)
        p = node.parent
        while p is not None and p.right is node:
            node = p
            p = p.parent
        return p

    def predecessor(self, node):
        if node.left is not None:
            return self.maxi(node.left)
        p = node.parent
        while p is not None and p.left is node:
            node = p
            p = p.parent
        return p

    def insert_helper(self, node, val):
        if val <= node.val:
            if node.left is not None:
                self.insert_helper(node.left, val)
            else:
                node.left = Node(val, parent=node)
        else:
            if node.right is not None:
                self.insert_helper(node.right, val)
            else:
                node.right = Node(val, parent=node)

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            self.median_node = self.root
            self.size = 1
            return

        self.insert_helper(self.root, val)
        if val > self.median:
            if self.size & 1:
                self.median_node = self.successor(self.median_node)
        else:
            if not self.size & 1:
                self.median_node = self.predecessor(self.median_node)
        self.size += 1

    @property
    def median(self):
        if self.size == 1:
            return self.root.val

        if self.size & 1:
            return self.median_node.val

        return (
            self.predecessor(self.median_node).val + self.median_node.val
        ) / 2

    def find(self, val):
        node = self.root
        while node and node.val != val:
            if val > node.val:
                node = node.right
            else:
                node = node.left
        return node

    def transplant(self, x, y):
        if x.parent is None:
            self.root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        if y is not None:
            y.parent = x.parent

    def delete(self, x):
        if x.left is None:
            self.transplant(x, x.right)
        elif x.right is None:
            self.transplant(x, x.left)
        else:
            mini = self.mini(x.right)
            if mini.parent is not x:
                self.transplant(mini, mini.right)
                mini.right = x.right
                mini.right.parent = mini
            self.transplant(x, mini)
            mini.left = x.left
            mini.left.parent = mini
        del x


def test1():
    t = Tree(4)
    print(t)
    print(t.median)
    print()
    for n in (2, 1, 1, 6, 6, 6):
        t.insert(n)
        print(t)
        print(t.median)
        print()


def test2():
    t = Tree()
    for n in (6, 10, 2, 6, 5, 0, 6, 3, 1, 0, 0):
        t.insert(n)
        print(t)
        print(t.median)
        print()


def test3():
    for _ in range(1000):
        numbers = [random.randint(-100, 100) for _ in range(20)]
        t = Tree()
        for n in numbers:
            t.insert(n)
        if t.median != statistics.median(numbers):
            print(t)


def test4():
    t = Tree(4)
    t.insert(2)
    t.insert(3)
    t.insert(1)
    t.insert(6)
    t.insert(5)
    t.insert(7)
    print(t.preorder())


def test5():
    t = Tree(4)
    t.insert(2)
    t.insert(3)
    t.insert(1)
    t.insert(6)
    t.insert(5)
    t.insert(7)
    print(t.postorder())



if __name__ == "__main__":
    test5()
