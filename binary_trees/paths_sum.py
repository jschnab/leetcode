# given a binary tree, return all the paths
# that sum to a given value
# a path does not necessarily starts at the root or ends at a leaf


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_paths(root, current_path, all_paths):
    if root:
        current_path = current_path + [root.val]
        if not root.left and not root.right:
            all_paths.append(current_path)
        get_paths(root.left, current_path, all_paths)
        get_paths(root.right, current_path, all_paths)


def subarray_sum(array, s, valid_paths):
    sum_ = 0
    path = []
    count = {0: 1}
    for i in array:
        sum_ += i
        path += i
        if count.get(sum_ - s):
            path += count.get(sum_ - s)
        count[sum_] = count.get(sum_, 0) + 1

def subarray_sum_brute(array, s, valid_paths):
    for i in range(len(array)):
        sum_ = 0
        path = []
        for j in range(i, len(array)):
            sum_ += array[j]
            path += array[j],
            if sum_ == s:
                valid_paths.append(path)


def paths_sum(root, s):
    all_paths = []
    get_paths(root, [], all_paths)
    valid_paths = []
    for path in all_paths:
        subarray_sum(path, s, valid_paths)
    return valid_paths


def test1():
    root = TreeNode(
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
    paths = []
    get_paths(root, [], paths)
    assert paths == [[1, 2, 4], [1, 2, 5], [1, 3, 6], [1, 3, 7]]
    print("test 1 successful")


def test2():
    root = TreeNode(
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
    paths = paths_sum(root, 7)
    assert paths == [[1, 2, 4], [2, 5], [7]]
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
