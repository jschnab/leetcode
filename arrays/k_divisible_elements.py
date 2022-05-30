"""
leetcode 2261: K divisible elements subarrays.

Given an integer array nums and two integers k and p, return the number of
distinct subarrays which have at most k elements divisible by p.

Two arrays A and B are distinct if:
* they are of different lengths
* there exists at least one index i where A[i] != B[i]

A subarray is defined as a non-empty contiguous sequence of elements in an
array.
"""


def n_subarrays(A, k, p):
    """
    """
    s = set()
    for i in range(len(A)):
        divisible = 0
        L = [str(A[i])]
        divisible += A[i] % p == 0
        if divisible <= k:
            s.add(",".join(L))
        for j in range(i + 1, len(A)):
            L.append(str(A[j]))
            divisible += A[j] % p == 0
            if divisible <= k:
                s.add(",".join(L))
    return len(s)


def test1():
    assert n_subarrays([2, 3, 3, 2, 2], 2, 2) == 11
    print("test 1 successful")


def test2():
    assert n_subarrays([1, 2, 3, 4], 4, 1) == 10
    print("test 2 successful")


def test3():
    assert n_subarrays([1, 9, 8, 7, 19], 1, 6) == 15
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
