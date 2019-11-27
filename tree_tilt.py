# script which finds the tilt of a binary tree

#class Node(object):
#   def __init__(self, x):
#       self.left = None
#       self.right = None
#       self.val = x

class Solution(object):
    def find_tilt(self, root):
        self.tilt = 0
        self.traverse(root)
        return self.tilt

    def traverse(self, root):
        if root is None:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.tilt += abs(left - right)
        return left + right + root.val
