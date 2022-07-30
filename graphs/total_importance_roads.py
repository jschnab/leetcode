"""
leetcode 2285: Maximum total importance of roads.

We are given an integer n denoting the number of cities in a country.

We are also given a 2D integer array roads where roads[i] = (a, b), indicating
there is a bidirectional road connecting cities a and b.

We need to assign each city with an integer value from 1 to n, where each value
can only be used once. The importance of a road is then defined as the sum of
the values of the two cities it connects.

Return the maximum total importance of all roads possible after assigning the
values optimally.
"""


def max_importance(n, roads):
    """
    Time complexity: O(nlogn) where n is the number of cites, because we sort
    cities by the number of connections.

    Space complexity: O(n) because we store a dictionary of cities and their
    connectivity, its sorted version, and the value of each city.

    :param int n: Number of cites.
    :param list(list(int)) roads: List of connected cities.
    :returns (int): Maximum importance of roads.
    """
    counts = {i: 0 for i in range(n)}
    for start, end in roads:
        counts[start] = counts.get(start, 0) + 1
        counts[end] = counts.get(end, 0) + 1
    sorted_counts = sorted(counts.items(), key=lambda x: x[1])
    values = {city: idx + 1 for idx, (city, _) in enumerate(sorted_counts)}
    result = 0
    for start, end in roads:
        result += values[start] + values[end]
    return result


def test1():
    roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
    assert max_importance(5, roads) == 43
    print("test 1 successful")


def test2():
    roads = [[0, 3], [2, 4], [1, 3]]
    assert max_importance(5, roads) == 20
    print("test 2 successful")


def test3():
    assert max_importance(5, [[0, 1]]) == 9
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
