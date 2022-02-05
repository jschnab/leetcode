from collections import deque

# given a directed graph, determine if there is a path between two nodes


def path_exists(graph, start, end):
    """
    Given a directed graph stored as a adjacency sets, determine if there
    is a path between a node holding the 'start' value and a node holding
    the 'end' value.

    :param dict graph: graph represented as a adjacency sets
    :param start: start value
    :param end: end value
    """
    explored = set()
    q = deque([start])
    while q:
        current = q.pop()
        if current == end:
            return True
        if current in explored:
            continue
        explored.add(current)
        for adjacent in graph.get(current, set()):
            q.appendleft(adjacent)
    return False


def test1():
    graph = {
        "A": {"B", "C"},
        "B": {"D"},
        "D": {"F"},
        "E": {"D"},
    }
    assert path_exists(graph, "A", "D") is True
    print("test 1 successful")


def test2():
    graph = {
        "A": {"B", "C"},
        "B": {"D"},
        "D": {"F"},
        "E": {"D"},
    }
    assert path_exists(graph, "A", "E") is False
    print("test 2 successful")


def test3():
    graph = {
        "A": {"B", "C"},
        "B": {"D"},
        "D": {"F"},
        "E": {"D"},
    }
    assert path_exists(graph, "C", "D") is False
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
