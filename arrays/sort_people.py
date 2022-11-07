"""
leetcode 2418: sort the people

We are given an array of strings N (names) and an array of distinct positive
integers H (heights), both of length n.

For each index i, N[i] and H[i] denote the name and height of the ith person.

Return N sorted in descending order by the people's heights.
"""


def people(N, H):
    return [s[0] for s in sorted(zip(N, H), key=lambda x: -x[1])]


def test1():
    names = ["Mary", "John", "Emma"]
    heights = [180, 165, 170]
    assert people(names, heights) == ["Mary", "Emma", "John"]
    print("test 1 successful")


def test2():
    names = ["Alice", "Bob", "Bob"]
    heights = [155, 185, 150]
    assert people(names, heights) == ["Bob", "Alice", "Bob"]
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
