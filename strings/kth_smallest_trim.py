"""
leetcode 2343: Query kth smallest trimmed number.

We are given an array of strings S, where each string is of equal length and
consists of only digits.

We are also given a 2D array of queries Q where Q[i] = (k, t). For each
query, we need to:

* trim each number in S to its rightmost t digits
* determine the index of the kth smallest trimmed number in S. If two trimmed
number are equal, the number with the lower index is considered to be smaller.
* reset each number in S to its original length before the next query

Return an array R of the same length as Q where R[i] is the result of the ith
query.

Notes:

* to trim to the rightmost x digits means to keep removing the leftmost digit
until only x digits remain
* strings in S may contain leading zeros
"""


def trim(S, Q):
    """
    Time complexity: O(qnlogn) where q is the number of queries and n is the
    number of elements in S.

    :param list(str) S: Strings of digits to be queried.
    :param list(list(int)) Q: Queries.
    :return (list(int)): Results.
    """
    result = []
    for k, t in Q:
        trimmed = [(s[-t:], i) for i, s in enumerate(S)]
        # We don't have to convert to int when sorting because all strings have
        # the same length so digits are aligned.
        trimmed.sort(key=lambda x: (x[0], x[1]))
        # k - 1 because of 0-based index
        result.append(trimmed[k - 1][1])
    return result


def test1():
    S = ["102", "473", "251", "814"]
    Q = [[1, 1], [2, 3], [4, 2], [1, 2]]
    assert trim(S, Q) == [2, 2, 1, 0]
    print("test 1 successful")


def test2():
    S = ["24", "37", "96", "04"]
    Q = [[2, 1], [2, 2]]
    assert trim(S, Q) == [3, 0]
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
