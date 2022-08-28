"""
leetcode 2343: Query kth smallest trimmed number.

We are given an array of strings S, where each string is of equal length and
consists of digits only.

We are also given a 2D integer array Q where Q[i] = [k, trim]. For each query
Q[i] we need to:

* trim each number in S to its rightmost trim digits
* determine the index of the kth smallest trimmed number. If two trimmed number
  are equal, the number with the lower index is considered to be smaller.
* reset each number to its original length for the next query

Return an array A of the same length as Q where A[i] is the answer to the query
Q[i].

Notes: Trim to the rightmost x digits means to remove the leftmost digits
until x digits remain. Strings in S may contain leading zeros.
"""


def k_trim(S, Q):
    """
    There is no need to convert S elements to integers because they have the
    same length.

    Time complexity: O(qnlogn) where q is the number of queries and n is the
    number of elements in S, because for each queries, we sort S.
    Space complexity: O(n) because we store a copy of S.

    :param list(str) S: Digit strings.
    :param list(list(int)) Q: Queries.
    """
    result = []
    for k, t in Q:
        trimmed = sorted(
            [(n[-t:], i) for i, n in enumerate(S)], key=lambda x: (x[0], x[1])
        )
        result.append(trimmed[k - 1][1])
    return result


def test1():
    S = ["102", "473", "251", "814"]
    Q = [[1, 1], [2, 3], [4, 2], [1, 2]]
    assert k_trim(S, Q) == [2, 2, 1, 0]
    print("test 1 successful")


def test2():
    S = ["24", "37", "96", "04"]
    Q = [[2, 1], [2, 2]]
    assert k_trim(S, Q) == [3, 0]
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
