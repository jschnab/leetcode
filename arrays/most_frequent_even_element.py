"""
leetcode 2404: most frequent even element

Given an integer array A, return the most frequent even element. If there is a
tie, return the smallest element. If there is no such element, return -1.
"""
from collections import Counter


def most_frequent(A):
    counts = Counter(i for i in A if not i & 1)
    if counts:
        return sorted(counts.items(), key=lambda x: (x[1], -x[0]))[-1][0]
    return -1


def test1():
    assert most_frequent([0, 1, 2, 2, 4, 4, 1]) == 2
    print("test 1 successful")


def test2():
    assert most_frequent([4, 4, 4, 9, 2, 4]) == 4
    print("test 2 successful")


def test3():
    assert most_frequent([1, 3, 5, 7, 7]) == -1
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
