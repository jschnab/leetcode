"""
leetcode 2178: Maximum split of positve even integer.

Given an integer N, the goal is to split it into a maximum number of unique
positive even integers.

For N = 12, the following splits are valid:

* 12
* 2 + 10
* 2 + 4 + 6
* 4 + 8

Among these splits, 2 + 4 + 6 contains the maximum number of items so this is
the solution.

2 + 2 + 4 + 4 is not valid (non-unique numbers).

Return the solution as a list of integers.
"""


def max_split(N):
    """
    Starting at 2, we grow the split list by iterating over even numbers.

    At each iteration, we ensure that the list sums up to N by subtracting
    the last list element from N.

    Time complexity: We iterate over even integers, up to N, so the time
    complexity is O(N).
    """
    # if N is not even, the solution is an empty list
    if N & 1:
        return []

    result = []
    cur = 2
    while N > 0:
        # if the sum will grow larger than N, we stop there by appending the
        # difference between the last list item and (original) N to the list
        if N - cur < cur + 2:
            result.append(N)
        else:
            result.append(cur)
        cur += 2
        N -= result[-1]
    return result


def test1():
    assert max_split(12) == [2, 4, 6]
    print("test 1 successful")


def test2():
    assert max_split(7) == []
    print("test 2 successful")


def test3():
    assert max_split(28) in (
        [2, 6, 8, 12],
        [2, 4, 10, 12],
        [2, 4, 6, 16],
    )
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
