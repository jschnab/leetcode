"""
leetcoe 2250: Count number of rectangles containing each point.

Given a 2D integer array R, where R[i] = (w, h) indicates that rectangle i has
width w and height h, and a 2D array P where P[i] = (x, y) is a point with
coordinates x and y.

Rectangle R[i] has its bottom left corner at (0, 0) and its top-right corner at
(w, h).

Return an integer array where item i is the number of rectangles that contain
P[i].

Points that lie on the edges of a rectangle are considered within the
rectangle.

Notes:

len(R), len(P) <= 100,000
h, y <= 100
w, x <= 1,000,000,000
"""

from collections import defaultdict


def brute_solution(R, P):
    """
    Time complexity: O(pr) with p = len(P) and r = len(R).
    Space complexity: O(p).
    """
    result = [0] * len(P)
    for i, (x, y) in enumerate(P):
        for w, h in R:
            if x <= w and y <= h:
                result[i] += 1
    return result


def binary_search(A, x):
    lo = 0
    hi = len(A) - 1
    result = len(A)
    while lo <= hi:
        mid = (lo + hi) // 2
        if A[mid] < x:
            lo = mid + 1
        else:
            result = mid
            hi = mid - 1
    return result


def count_rectangles(R, P):
    """
    We can improve the time complexity of the brute-force solution by sorting
    rectangles by width (the dimension that has the highest cardinality) and
    perform binary search on width to find rectangles that contain a given
    point. Since rectangles heights have a low cardinality (100), we keep a
    linear search on height.

    Time complexity: O(p * h * log(w)) with p = len(P), h = cardinality of
    rectangle heights, and w = cardinality of rectangle widths.
    Space complexity: O(h * len(R)) with h = cardinality of rectangle heights.
    """
    d = defaultdict(list)
    for w, h in R:
        d[h].append(w)
    for h, w in d.items():
        w.sort()
    result = []
    for x, y in P:
        count = 0
        for i in range(y, 101):
            if i in d:
                count += len(d[i]) - binary_search(d[i], x)
        result.append(count)
    return result


def test1():
    R = [[1, 2], [2, 3], [2, 5]]
    P = [[2, 1], [1, 4]]
    assert brute_solution(R, P) == [2, 1]
    assert count_rectangles(R, P) == [2, 1]
    print("test 1 successful")


def test2():
    R = [[1, 1], [2, 2], [3, 3]]
    P = [[1, 3], [1, 1]]
    assert brute_solution(R, P) == [1, 3]
    assert count_rectangles(R, P) == [1, 3]
    print("test 2 successful")


def test3():
    R = [[7, 1], [2, 6], [1, 4], [5, 2], [10, 3], [2, 4], [5, 9]]
    P = [[10, 3], [8, 10], [2, 3], [5, 4], [8, 5], [7, 10], [6, 6], [3, 6]]
    assert brute_solution(R, P) == [1, 0, 4, 1, 0, 0, 0, 1]
    assert count_rectangles(R, P) == [1, 0, 4, 1, 0, 0, 0, 1]
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
