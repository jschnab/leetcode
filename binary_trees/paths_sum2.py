# given a binary tree, return all the paths
# that sum to a given value
# a path does not necessarily starts at the root or ends at a leaf


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


def print_path(path, start, end):
    print("->".join(str(i) for i in path[start:end+1]))


def find_sum(root, target, path, level):
    if not root:
        return

    path = path + [root.val]
    total = 0
    for i in range(level, -1, -1):
        total += path[i]
        if total == target:
            print_path(path, i, level)

    find_sum(root.left, target, path, level+1)
    find_sum(root.right, target, path, level+1)


def test1():
    t = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3, TreeNode(4), TreeNode(5))
    )
    assert height(t) == 3
    print("test 1 successful")


def test2():
    t = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(4),
            TreeNode(5)
        ),
        TreeNode(
            3,
            TreeNode(6),
            TreeNode(7)
        )
    )
    find_sum(t, 7, [], 0)


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
