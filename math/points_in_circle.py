"""
leetcode 2249: Count lattice points inside a circle.

Given a 2D array A where A[i] = (x, y, r) represents the center (x, y) and
radius r of a circle, return the number of lattice points that are present
inside at least one circle.

A lattice point is a point with integer coordinates.
Points that lie on the circumference of a circle are also inside it.
"""

import math


def get_points(x, y, r):
    points = set()
    for j in range(x - r, x + r + 1):
        for i in range(y - r, y + r + 1):
            if math.sqrt((x - j)**2 + (y - i)**2) <= r:
                # could use math.dist in python >= 3.8
                points.add((j, i))
    return points


def count_points(A):
    points = set()
    for x, y, r in A:
        points.update(get_points(x, y, r))
    return len(points)


def test1():
    assert count_points([(2, 2, 2), (3, 4, 1)]) == 16
    print("test 1 successful")


def test2():
    assert count_points([(2, 2, 1)]) == 5
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
