# leetcode challenge 257: binary tree paths
# given a binary tree, return all root-to-leaf paths

# input:  [1,2,3,null,5,null,null]
# output: ["1->2->5", "1->3"]


def helper(node, path, result):
    if node:
        if path != "":
            path += "->"
        path += str(node.val)
        dfs(node.left, path, result)
        dfs(node.left, path, result)
        if not node.left and not node.right:
            result.append(path)


def tree_paths(root):
    result = []
    dfs(root, "", result)
    return result

