"""
Given a string S that contains 0 or 1 at each position (0 is an office building
and 1 is a restaurant). A city official would like to select 3 building for
random inspections such that no two consecutive selected building are the same
type.

Return the number of valid ways to select buildings.
"""


def select_buildings(S):
    """
    We could count the number of common subsequences between 010 and the
    input string, then between 101 and the input string (010 and 101 are the
    strings that satisfy the problem constraints).

    Since the string can only contain 0 or 1, we can directly count the number
    of subsequences that match 0, 1, 01, 10, 101, and 010.

    Time complexity: O(length(S)).
    Space complexity: O(1).
    """
    count = dict(zip(["0", "1", "01", "10", "010", "101"], [0] * 6))
    for c in S:
        if c == "0":
            count["0"] += 1
            count["10"] += count["1"]
            count["010"] += count["01"]
        else:
            count["1"] += 1
            count["01"] += count["0"]
            count["101"] += count["10"]
    return count["101"] + count["010"]


def test1():
    assert select_buildings("001101") == 6
    print("test 1 successful")


def test2():
    assert select_buildings("11100") == 0
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
