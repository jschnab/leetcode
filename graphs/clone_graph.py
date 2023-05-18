"""
leetcode 133: clone graph

Given a reference of a node in a connected undirected graph, return a deep copy
(clone) of the graph.

Each node in the graph contains an int value and a list of node objects that
represents its neighbors.
"""


class Node:
    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = neighbors or []


def clone(node):
    """
    We traverse the graph from the input node using depth-first search and add
    vertices and edges to the graph clone.

    We store the graph clone in a dictionary that maps vertex value to vertex
    object to efficiently retrieve any existing vertex if it's already copied.
    This dictionary also allows us to keep track of visited vertices.
    """
    if node is None:
        return
    clone = {node.val: Node(node.val)}
    stack = [node]
    while stack != []:
        cur = stack.pop()
        for nb in cur.neighbors:
            if nb.val not in clone:
                stack.append(nb)
                clone[nb.val] = Node(nb.val)
            clone[cur.val].neighbors.append(clone[nb.val])
    return clone[node.val]


def get_vertex(start, target):
    seen = set()
    stack = [start]
    while stack != []:
        cur = stack.pop()
        if cur.val == target:
            return cur
        for nb in cur.neighbors:
            if nb.val not in seen:
                stack.append(nb)
        seen.add(cur.val)


def get_neighbors_values(vertex):
    return [nb.val for nb in vertex.neighbors]


def test1():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    one.neighbors = [two, four]
    two.neighbors = [one, three]
    three.neighbors = [two, four]
    four.neighbors = [three, one]
    copy = clone(one)
    assert get_neighbors_values(get_vertex(copy, 1)) == [2, 4]
    assert get_neighbors_values(get_vertex(copy, 2)) == [1, 3]
    assert get_neighbors_values(get_vertex(copy, 3)) == [2, 4]
    assert get_neighbors_values(get_vertex(copy, 4)) == [3, 1]
    print("test 1 successful")


def test2():
    one = Node(1)
    copy = clone(one)
    assert copy.val == 1
    assert copy.neighbors == []
    print("test 2 successful")


def test3():
    copy = clone(None)
    assert copy is None
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
