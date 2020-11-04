# make a binary search tree with minimum height from a sorted (ascending) array


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_from_array(array):
    return helper(array, None)


def helper(array, root):
    if not array:
        return
    mid = len(array) // 2
    root = TreeNode(array[mid])
    root.left = helper(array[:mid], root.left)
    root.right = helper(array[mid+1:], root.right)
    return root



def test1():
    assert tree_from_array([]) is None
    print("test 1 successful")


def test2():
    root = tree_from_array([1])
    assert root.val == 1 and not root.left and not root.right
    print("test 2 successful")


def test3():
    root = tree_from_array([1, 2])
    assert root.val == 2 and root.left.val == 1 and not root.right
    print("test 3 successful")


def test3():
    root = tree_from_array([1, 2])
    assert root.val == 2 and root.left.val == 1 and not root.right
    print("test 3 successful")


def test4():
    root = tree_from_array([1, 2, 3])
    assert root.val == 2 \
        and root.left.val == 1 \
        and root.right.val == 3
    print("test 4 successful")


def test5():
    root = tree_from_array([1, 2, 3, 4, 5])
    assert root.val == 3 \
        and root.left.val == 2 \
        and root.left.left.val == 1 \
        and root.right.val == 5 \
        and root.right.left.val == 4
    print("test 5 successful")


def test6():
    root = tree_from_array([1, 2, 3, 4])
    assert root.val == 3 \
        and root.left.val == 2 \
        and root.left.left.val == 1 \
        and root.right.val == 4
    print("test 6 successful")




def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()


if __name__ == "__main__":
    main()
