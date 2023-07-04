"""
leetcode 2579: count total number of colored cells

There exists an infinitely large 2D grid of uncolored cells. You are given a
positive integer n, indicating that you must do the following routine for n
minutes:

* At the first minute, color any arbitrary unit cell blue.
* Every minute thereafter, color blue every uncolored cell that touches a blue
  cell.

Return the number of colored cells at the end of n minutes
"""


def color_cells(n):
    # We notice that every minute, the number of new colored cells is 4 more
    # than the previous minute (+4, +8, +12, etc.).
    result = 1
    for i in range(1, n):
        result += i * 4
    return result


def color_cells2(n):
    # We directly calculate the sum of the n terms of the arithmetic series of
    # reason 4 and first term 0: S = n/2*(2*a + d*(n-1)) where a is the first
    # term.
    return 1 + n * (4 * (n - 1)) // 2


def color_cells3(n):
    # We notice the sequence follows centered square numbers:
    # https://oeis.org/A001844
    # The formula is adjusted to give 1 when n = 1.
    return 2 * n * (n - 1) + 1


def test1():
    assert color_cells(1) == 1
    assert color_cells2(1) == 1
    assert color_cells3(1) == 1
    print("test 1 successful")


def test2():
    assert color_cells(2) == 5
    assert color_cells2(2) == 5
    assert color_cells3(2) == 5
    print("test 2 successful")


if __name__ == "__main__":
    test1()
    test2()
