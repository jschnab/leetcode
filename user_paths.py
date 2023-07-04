from collections import defaultdict
from datetime import datetime


class TreeNode:
    def __init__(
        self,
        action=None,
        count=None,
        paths=None,
        path_index=None,
    ):
        self.action = action
        self.count = count
        self.paths = paths
        self.path_index = path_index
        self.children = []

    def build_children(self):
        action_count = defaultdict(int)
        sub_paths = defaultdict(dict)
        for userid, actions in self.paths.items():
            if self.path_index < len(actions):
                action_count[actions[self.path_index]] += 1
                sub_paths[actions[self.path_index]][userid] = actions
        for action, count in action_count.items():
            node = TreeNode(
                action,
                count,
                sub_paths[action],
                self.path_index + 1,
            )
            self.children.append(node)
            node.build_children()


def process_logs(logs):
    user_paths = defaultdict(list)
    for userid, ts, action in logs:
        user_paths[userid].append(action)
    root = TreeNode(paths=user_paths, path_index=0)
    root.build_children()
    return root


def traverse_tree(root, level):
    if root.action is not None:
        print(f"{' ' * level}{root.action} {root.count}")
        level += 2
    for child in root.children:
        traverse_tree(child, level)


if __name__ == "__main__":
    logs = [
        (1, datetime.now(), "A"),
        (1, datetime.now(), "B"),
        (2, datetime.now(), "A"),
        (2, datetime.now(), "C"),
        (1, datetime.now(), "D"),
        (3, datetime.now(), "B"),
        (3, datetime.now(), "C"),
        (4, datetime.now(), "B"),
    ]

    root = process_logs(logs)
    traverse_tree(root, 0)
