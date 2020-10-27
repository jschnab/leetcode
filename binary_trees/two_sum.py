# leetcode challenge 653: two sum IV - binary search tree
# given the root of a BST and a target number k, return True if there exist
# two elements in the tree such that their sum is equal to the given target

# input:  [5,3,6,2,4,null,7], k = 9
# output: True

# input:  [5,3,6,2,4,null,7], k = 28
# output: False


def two_sum_iter(root, k):
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    values = set()
    stack = [root]

    # preorder traversal
    while stack:
        node = stack.pop()
        val = node.val
        if (k - val) in values:
            return True
        values.add(val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return False


def helper(root, k, hashset):
    if root:
        if (k - root.val) in hashset:
            return True
        hashset.add(root.val)
        return helper(root.left, k, hashset) or helper(root.left, k, hashset)
    return False


def two_sum_recur(root, k):
    return helper(root, k, set())
