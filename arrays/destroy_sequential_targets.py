"""
We are given an array A consisting of positive integers, representing targets
on a number line. We are also given an integer 'space'.

We have a machine that can destroy targets. Seeding the machine with some A[i]
allows it to destroy all targets with values that can be represented as
A[i] + c * space where c is any non-negative integer. We want to destroy the
maximum number of targets in A.

Return the minimum value of A[i] we can seed the machine with to destroy the
maximum number of targets.
"""

from collections import defaultdict


def destroy(A, space):
    count = defaultdict(int)
    for n in A:
        count[n % space] += 1
    result = A[0]
    for n in A[1:]:
        if count[result % space] == count[n % space]:
            result = min(result, n)
        elif count[result % space] < count[n % space]:
            result = n
    return result


def test1():
    assert destroy([3, 7, 8, 1, 1, 5], 2) == 1
    print("test 1 successful")


def test2():
    assert destroy([1, 3, 5, 2, 4, 6], 2) == 1
    print("test 2 successful")


def test3():
    assert destroy([6, 2, 5], 100) == 2
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
