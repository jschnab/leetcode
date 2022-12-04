"""
leetcode 2442: count number of distinct integers after reverse operations.

We are given an array A consisting of positive integers.

We have to take each integer in the array, reverse its digits, and add it to
the end of the array. We should apply this operation to the original integers
in A.

Return the number of distrinct integers in the final array.
"""


def rev(n):
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n //= 10
    return result


def count_distinct(A):
    for i in range(len(A)):
        A.append(rev(A[i]))
    return len(set(A))


def test1():
    assert count_distinct([1, 13, 10, 12, 31]) == 6
    print("test 1 successful")


def test2():
    assert count_distinct([2, 2, 2]) == 1
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
